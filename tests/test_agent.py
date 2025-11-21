import pytest
from src.workflow import build_orchestrator
from src.tools import SaveBriefTool

def test_orchestrator_structure():
    """Verify the orchestrator is built with 3 agents."""
    agent = build_orchestrator()
    # --- FIX: Check 'steps' instead of 'agents' ---
    assert len(agent.steps) == 3
    assert agent.name == 'OmniChannel_Strategist_Orchestrator'

def test_tools_assignment():
    """Verify the Strategist agent has the custom SaveBriefTool."""
    agent = build_orchestrator()
    # --- FIX: Access 'steps' instead of 'agents' ---
    # Access the strategist (2nd agent in sequence)
    strategist = agent.steps[1]
    
    # Helper to check tools safely (handles different ADK versions)
    # Some versions store tools in a list, others in a dictionary
    assert strategist.tools is not None
    
    # Check if our tool is present by looking at the tool object
    has_save_tool = False
    for tool in strategist.tools:
        # Check against the function name we defined in src/tools.py
        if tool.fn.__name__ == 'save_content_brief_to_state':
            has_save_tool = True
            break
            
    assert has_save_tool, "Strategist agent should have the save_brief tool assigned."

def test_json_cleaner_logic():
    """Test if our tool function correctly strips Markdown."""
    from src.tools import save_content_brief_to_state
    
    # Simulated LLM output with markdown
    mock_input = '```json\n{"topic": "Test", "target_platform": "X"}\n```'
    result = save_content_brief_to_state(mock_input)
    
    assert "SUCCESS" in result
