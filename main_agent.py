import json # F401: Used by save_content_brief_to_state
import os 
from typing import Dict, Any

from google.adk.agents import Agent
from google.adk.agents.workflow import SequentialAgent
from google.adk.tools import google_search, FunctionTool

# --- CONFIGURATION ---
MODEL_NAME = 'gemini-2.5-flash' 

# ----------------------------------------------------------------------
## 1. Define Custom Tool (Structured Output/Mock Integration)

def save_content_brief_to_state(brief_json: str) -> str:
    """Saves the structured content brief (JSON string) to a simulated database. 
    This is an example of a custom tool the agent can call."""
    try:
        # F821: This was the original error (fixed by 'import json')
        brief_data = json.loads(brief_json) 
        print(f"**[Tool Called]** Saving Strategy: Topic='{brief_data.get('topic')}'")
        return "SUCCESS: Content brief saved and ready for the drafting agent."
    except Exception as e:
        return f"ERROR: Failed to parse and save brief. Please ensure output is valid JSON. Error: {e}"

# Register the custom function as a tool
SaveBriefTool = FunctionTool(
    name="save_brief", 
    description="Tool for saving the final structured content brief as a JSON string to the database."
)


# ----------------------------------------------------------------------
## 2. Define Specialist Agents

# 2.1. Market Research Agent (Uses Tool)
research_agent = Agent(
    model=MODEL_NAME,
    name='Market_Research_Agent',
    description='Specialist in web research and competitive analysis.',
    instruction=(
        'You are an expert market researcher. Use the Google Search tool to find 3 key competitive '
        'strategies and 3 current trends for the given user request. Summarize concisely.'
    ),
    tools=[google_search] 
)

# 2.2. Content Strategist Agent (Uses Structured Output/Tool)
strategist_agent = Agent(
    model=MODEL_NAME,
    name='Content_Strategist_Agent',
    description='Generates a structured JSON content brief and calls the save_brief tool.',
    instruction=(
        'You are a strategic planner. Based on the research provided, define a Content Brief. '
        'Your output MUST be a valid JSON object with keys: "topic", "target_platform" (e.g., Twitter), '
        '"keywords", "call_to_action", and "main_talking_points" (list of strings). '
        'Once generated, you MUST call the `save_brief` tool with the full JSON string.'
    ),
    tools=[SaveBriefTool]
)

# 2.3. Content Generator Agent 
generator_agent = Agent(
    model=MODEL_NAME,
    name='Content_Generator_Agent',
    description='Drafts platform-specific content based on a structured brief.',
    instruction=(
        'You are a professional copywriter. Using the Content Brief from the system state, write a '
        '280-character Twitter post. Focus on the CTA and use the defined keywords.'
    ),
)


# ----------------------------------------------------------------------
## 3. Define the Orchestrator (The Main Agent)

# The SequentialAgent runs the sub-agents in the exact order specified.
root_agent = SequentialAgent(
    name='OmniChannel_Strategist_Orchestrator',
    description='Manages the end-to-end process: research, strategy, and content drafting.',
    # The agents run one after the other. The output of one becomes input for the next.
    agents=[
        research_agent,        # Step 1: Research the market
        strategist_agent,      # Step 2: Create structured plan and save it
        generator_agent        # Step 3: Draft content using the structured plan
    ]
)

# This block allows you to run the agent interactively when the file is executed.
if __name__ == '__main__':
    # Placeholder for the ADK Runner or Session logic if run independently
    print("Agent modules defined successfully. Use 'adk run' or a dedicated runner script to execute the agent.")
    pass
