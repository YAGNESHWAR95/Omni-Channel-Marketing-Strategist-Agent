import json
from google.adk.tools import FunctionTool

def save_content_brief_to_state(brief_json: str) -> str:
    """
    Saves the structured content brief (JSON string) to a simulated database. 
    """
    try:
        # 1. Clean the input: Remove Markdown code blocks if the LLM added them
        clean_json = brief_json.strip()
        if clean_json.startswith("```"):
            # Remove first line (```json) and last line (```)
            lines = clean_json.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].strip() == "```":
                lines = lines[:-1]
            clean_json = "\n".join(lines)

        # 2. Parse JSON
        brief_data = json.loads(clean_json)
        
        # 3. Simulate Database Save
        topic = brief_data.get('topic', 'Unknown Topic')
        print(f"\n>> [TOOL ACTION] Saving Strategy to DB: {topic}")
        print(f">> [TOOL DATA] Target Platform: {brief_data.get('target_platform')}")
        
        return "SUCCESS: Content brief validated and saved to database."
    
    except json.JSONDecodeError:
        return "ERROR: Output was not valid JSON. Please retry formatting."
    except Exception as e:
        return f"ERROR: Failed to save brief. {str(e)}"

# --- THE FIX IS HERE ---
# We pass the function directly. The ADK reads the name 'save_content_brief_to_state'
# and the docstring above automatically.
SaveBriefTool = FunctionTool(save_content_brief_to_state)
