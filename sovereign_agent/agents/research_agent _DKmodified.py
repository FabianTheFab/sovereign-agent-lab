"""
sovereign_agent/agents/research_agent.py
=========================================
The Research Agent for your Sovereign Agent project.

This is the file that grows each week:

  Week 1 (now):    Basic ReAct loop with 4 venue tools
  Week 2:          Add real web search and file operation tools
  Week 3:          Split into Planner (DeepSeek R1) + Executor (Llama 70B)
  Week 4:          Add CLAUDE.md memory so the agent remembers past sessions
  Week 5:          Add observability, cost tracking, and safety guardrails

The public interface — run_research_agent(task, max_turns) → dict — stays the
same across all weeks. Week 2's code imports and calls this function exactly
as Week 1 leaves it. You add capability inside; the callers don't change.

HOW TO USE
----------
Import and call from exercise files:

    from sovereign_agent.agents.research_agent import run_research_agent

    result = run_research_agent(
        task="Find a pub for 160 vegan guests tonight.",
        max_turns=8,
    )
    print(result["final_answer"])
    print(result["tool_calls_made"])

ADDING TOOLS IN FUTURE WEEKS
-----------------------------
To add a new tool, import it and add it to the TOOLS list below.
The agent picks up the new capability automatically — no other changes needed.

    # Week 2 example:
    from sovereign_agent.tools.web_search import search_web
    TOOLS = [
        check_pub_availability,
        get_edinburgh_weather,
        calculate_catering_cost,
        generate_event_flyer,
        search_web,           # ← just add here
    ]
"""

import json
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Import tools from the shared tool layer
# This import path is why the project structure matters —
# sovereign_agent/ is a Python package that can be imported from anywhere
from sovereign_agent.tools.venue_tools import (
    check_pub_availability,
    get_edinburgh_weather,
    calculate_catering_cost,
    generate_event_flyer,
)

load_dotenv()

# ─── Model ────────────────────────────────────────────────────────────────────
# Week 1: single model handles everything
# Week 3: this gets split into llm_planner (DeepSeek R1) and llm_executor (Llama 70B)

llm = ChatOpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_KEY"),
    model="Qwen/Qwen3-32B",
    temperature=0,
    extra_body={"thinking": {"type": "disabled"}},
)

# ─── Tool registry ────────────────────────────────────────────────────────────
# Week 1: 4 venue tools
# Week 2: add search_web, read_file, write_file here

TOOLS = [
    check_pub_availability,
    get_edinburgh_weather,
    calculate_catering_cost,
    generate_event_flyer,
]

# Build the agent once at module load time.
# Rebuilding it on every call would be wasteful.
_agent = create_react_agent(llm, TOOLS)


# ─── Public interface ─────────────────────────────────────────────────────────

def run_research_agent(task: str, max_turns: int = 8) -> dict:
    result = _agent.invoke(
        {"messages": [("user", task)]},
        config={"recursion_limit": max_turns * 2},
    )

    tool_calls_made = []
    full_trace      = []
    final_answer    = ""

    for m in result["messages"]:
        role    = getattr(m, "type", "unknown")
        content = m.content

        # FIX: LangChain/OpenAI protocol puts tool calls in message.tool_calls,
        # not in content blocks — the original code was looking for Anthropic format
        if hasattr(m, "tool_calls") and m.tool_calls:
            for tc in m.tool_calls:
                entry = {"tool": tc["name"], "args": tc.get("args", {})}
                tool_calls_made.append(entry)
                full_trace.append({"role": "tool_call", **entry})
            continue

        if content:
            full_trace.append({"role": role, "content": str(content)})
            if role == "ai":
                final_answer = str(content)

    return {
        "final_answer":    final_answer,
        "tool_calls_made": tool_calls_made,
        "full_trace":      full_trace,
        "success":         bool(final_answer),
    }
