import os
from google.adk.agents import Agent, LlmAgent
from google.adk.agents.workflow import SequentialAgent
from google.adk.tools import google_search # Built-in tool for RAG
from google.adk.tools import FunctionTool
from typing import Dict, Any
import json

# --- CONFIGURATION (Ensure GOOGLE_API_KEY is set in your .env file) ---
MODEL_NAME = 'gemini-2.5-flash' # Good balance of speed and capability

# ----------------------------------------------------------------------
## 1. Define Custom Tool (Example: Structured Output/Mock Integration)

# This Pydantic model defines the structure of the data the Content Strategist MUST output.
# You would use a library like pydantic for production, but for ADK instruction,
# you define the schema in the instruction prompt.

def save_content_brief_to_state(brief_json: str) -> str:
    """Saves the structured content brief (JSON string) to a simulated database. 
    This is an example of a custom tool the agent can call."""
    try:
        # In a real app, you'd parse brief_json and save it to a database
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
    instruction='You are an expert market researcher. Use the Google Search tool to find 3 key competitive strategies and 3 current trends for the given user request. Summarize concisely.',
    description='Specialist in web research and competitive analysis.',
    tools=[google_search] 
)

# 2.2. Content Strategist Agent (Uses Structured Output/Tool)
# The output_key ensures the result is passed into the Sequential Agent's state.
strategist_agent = Agent(
    model=MODEL_NAME,
    name='Content_Strategist_Agent',
    instruction='''You are a strategic planner. Based on the research provided, define a Content Brief. 
        Your output MUST be a valid JSON object with keys: "topic", "target_platform" (e.g., Twitter), 
        "keywords", "call_to_action", and "main_talking_points" (list of strings).
        Once generated, you MUST call the `save_brief` tool with the full JSON string.
        ''',
    description='Generates a structured JSON content brief and saves it.',
    tools=[SaveBriefTool]
)

# 2.3. Content Generator Agent 
generator_agent = Agent(
    model=MODEL_NAME,
    name='Content_Generator_Agent',
    instruction='You are a professional copywriter. Using the Content Brief from the system state, write a 280-character Twitter post. Focus on the CTA and use the defined keywords.',
    description='Drafts platform-specific content based on a structured brief.',
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

# Optional: Add a simple function to run the agent (for testing)
async def run_marketing_agent(prompt: str):
    """Runs the main agent with a user prompt."""
    print(f"--- Running Agent with Prompt: {prompt} ---")
    
    # In a full ADK environment, you would use a Runner or Session
    # For a simple notebook test, you can often call the agent directly (ADK handles the state flow).
    result = await root_agent(prompt)
    
    print("\n--- FINAL RESULT ---")
    print(result.text)
    
# --- END OF agent.py ---
