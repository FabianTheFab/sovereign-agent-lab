"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

"""
NOTE from DK: Task was completed with changed code for the research agent (see research_agent_DKmodified)
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = ""   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-73371d05-b066-4c96-9b37-cf21976bd67f_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The user wanted to check The Bow Bar first for 160 vegan guests. The first tool response showed that The Bow Bar's capacity is only 80, which is too small. So then I checked The Albanach next. The response for The Albanach says it has a capacity of 180, which is more than 160, and it meets all constraints, including vegan options. So that's a good fit.
"""

SCENARIO_1_FALLBACK_VENUE = "Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
<think>\nOkay, let's see. The user wants a venue for 300 people with vegan options. I checked all four known pubs: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar.\n\nThe first two had vegan options but not enough capacity. The Guilford Arms had enough space but no vegan options. The Bow Bar has vegan options but is too small and is already full. None of them meet both the capacity and availability requirements. So, I need to tell the user that none of the known venues can accommodate their event. Maybe suggest looking for other places outside the known list or adjusting the requirements.\n</think>\n\nNone of the known Edinburgh venues can accommodate 300 people with vegan options. The largest available space (The Guilford Arms) holds 200 but lacks vegan options, while venues with vegan options (Albanach, Haymarket Vaults, Bow Bar) have capacities of 180, 160, and 80 respectively. Would you like to consider alternative solutions like booking multiple venues or adjusting requirements?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "<think>\nOkay, the user is asking about the last train time from Edinburgh Waverley to London tonight. Let me check the tools provided.\n\nLooking at the available functions: check_pub_availability, get_edinburgh_weather, calculate_catering_cost, generate_event_flyer. None of these are related to train schedules. The functions are for checking pub availability, weather, catering costs, and generating flyers. \n\nSince there's no tool for train times, I can't use any of the provided functions to answer this. I need to inform the user that I don't have the capability to provide train schedule information. I should apologize and suggest they check a train service website or app for real-time updates.\n</think>\n\nI don't have access to real-time train schedules or transportation data. For the most accurate information about the last train from Edinburgh Waverley to London, I recommend checking:\n1. The National Rail website (www.nationalrail.co.uk)\n2. Train operator apps like LNER or ScotRail \n3. Real-time platforms like Citymapper or Google Maps\n\nWould you like help with anything related to Edinburgh pubs, weather, event planning, or catering calculations?"

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
This behavior is acceptable in a bare-bones tech demo version of a real booking assistant. The full product should have stronger functionality and ability to interact with booking for transport as well. However, it is a positive sign that the model recognized its limitations and did not provide a false positive answer.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---\nconfig:\n  flowchart:\n    curve: linear\n---\ngraph TD;\n\t__start__([<p>__start__</p>]):::first\n\tagent(agent)\n\ttools(tools)\n\t__end__([<p>__end__</p>]):::last\n\t__start__ --> agent;\n\tagent -.-> __end__;\n\tagent -.-> tools;\n\ttools --> agent;\n\tclassDef default fill:#f2f0ff,line-height:1.2\n\tclassDef first fill-opacity:0\n\tclassDef last fill:#bfb6fc\n
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph demonstrates a model which has freedom to call any tools in any order to achieve the goal. There are fewer guardrails and safety regulations because the structure of the execution is not specified. Meanwhile, Rasa CALM has a very specific flow of events, with the agent responsible only for calling a given flow, with pre-defined sequence inside.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
Besides the initial error with the code, which was rather surprising, I had not met any unexpected behaviour. The more powerful model successfully overcame all edge cases in task C, and barring the rather low-quality poster from Task B it has done the task with no apparent issue. 
"""
