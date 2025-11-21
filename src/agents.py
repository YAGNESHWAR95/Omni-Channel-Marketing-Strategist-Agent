from google.adk.agents import Agent
from google.adk.tools import google_search
from src.config import MODEL_NAME
from src.tools import SaveBriefTool

# 1. Market Research Agent
research_agent = Agent(
    model=MODEL_NAME,a
    name='Market_Research_Agent',
    description='Specialist in web research and competitive analysis.',
    instruction=(
        'You are an expert market researcher. Use the Google Search tool to find 3 key competitive '
        'strategies and 3 current trends for the given user request. '
        'Summarize the findings concisely.'
    ),
    tools=[google_search] 
)

# 2. Content Strategist Agent
strategist_agent = Agent(
    model=MODEL_NAME,
    name='Content_Strategist_Agent',
    description='Generates a structured JSON content brief and calls the save tool.',
    instruction=(
        'You are a strategic planner. Based on the research provided, define a Content Brief. '
        'Your output MUST be a valid JSON object with keys: "topic", "target_platform" (e.g., Twitter), '
        '"keywords", "call_to_action", and "main_talking_points" (list of strings). '
        # UPDATED INSTRUCTION BELOW:
        'Once generated, you MUST call the `save_content_brief_to_state` tool with the full JSON string.'
    ),
    tools=[SaveBriefTool]
)

# ... (rest of file remains the same)

# 3. Content Generator Agent 
generator_agent = Agent(
    model=MODEL_NAME,
    name='Content_Generator_Agent',
    description='Drafts platform-specific content based on a structured brief.',
    instruction=(
        'You are a professional copywriter. Using the Content Brief from the system state, write a '
        'high-impact marketing post. Adopt the tone specified in the strategy. '
        'Ensure you include the Call to Action.'
    ),
)
