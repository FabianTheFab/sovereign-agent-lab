"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

"""
NOTE from DK: Task was completed with changed code for the research agent (see exercise4_mcp_client_DKmodified)
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues","get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "It seems there are no Edinburgh venues currently available that can accommodate 300 people with vegan options. Would you like to adjust your search criteria (e.g., lower the capacity requirement or check for other dietary options)?"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
We only updated mcp_venue_server.py resulting in the program not recognising Albanach as a viable option. Only Haymarket was mentioned in the results, giving us the only possible answer. This is consistent with the expectations.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 28   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
We provide a standard protocol for interaction with the tools. This allows any agent to discover and use them, and we do not need to interact with the client to update or otherwise change the server and the tools.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- The complete agent will be of the OpenClaw Automator class. According to the provided specs, it will plan autonomously, execute tools, store results in memory, and send a summary after.
- It begins with the foundational layer of tools for data interaction. These are python-coded instruments that it could use.
- These need to be expanded with the second layer of tools: live web search and file read/write.
- Another important component is the creation of thinking "planner" part and quick "executor" part which would work in tande, to deliver results.
- Finally, it will require proper heartbeat scheduling to make it run constantly but without overspending tokens/falling into an error loop.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The OpenClaw Automator should be used for research, while the Rasa Digital Employee should be used for the call. The reasons are evident from the observed behaviour: the former is capable of coming up with solutions and ideas outside the scope of provided information (see the suggestions for transportation in Ex2), while the latter is neatly structured and guarantees security with human interaction involved (see Ex3 for attempts to go off script prevented by the flows). Swapping them would create a narrow-minded researcher who cannot experiment as well as a very carefree caller who can make judgements without human double-checking it.
"""
