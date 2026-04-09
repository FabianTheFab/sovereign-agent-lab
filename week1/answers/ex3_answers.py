"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  160 guests


Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  GBP 200 deposit
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

#DK: I have no idea why Provider List: https://docs.litellm.ai/docs/providers appears above, but I included it as per instructions

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  160 guests

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan

Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

What deposit amount in GBP are you proposing to secure the booking?
Your input ->  GBP 1000 deposit
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £1000 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?

"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "deposit of £1000 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  160 guests


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for speake
rs?
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
It responded with the reasonable comment on limits of its capabilities and provided a way to return to the original script as well as an option to escalate further.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
As expected, LangGraph provided a more thorough answer with external sources when faced with the unexpected out-of-scope problem. Meanwhile, CALM behaved as programmed: it ran the error flow first and primed itself to continue with the primary flow. This fully coincides with the designed procedure.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["sovereign-agent-lab/exercise3_rasa/actions/action.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I have changed system time to be after 16:45 and ran with the "happy path" script. It has gone well until the last moment where the model has raised the concern regarding insufficient time - "it is past 16:45 — insufficient time to process the confirmation before the 5 PM deadline", to quote.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
While I have no experience with "Old Rasa" as this is not the part of the course, I believe the following is correct:

- LLM handles parsing of user inputs, which is more convinient in terms of programming and user experience, but costs tokens.
- Python is still used to hard-limit business rules and guarantee that the model cannot talk around them.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
Rasa CALM agent cannot provide external advice or direction, since it is literally programmed to follow the given flow. It can be considered a feature, since we do not want it to be able to improvise untrained responses or call imaginary tools. By sacrificing some freedom, we gain a more robust app, which is more useful for human interaction.
"""
