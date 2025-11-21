import pytest
from src.workflow import build_orchestrator

def test_orchestrator_structure():
    """Verify the orchestrator is built correctly."""
    agent = build_orchestrator()
    
    # Check for 'sequence'
    if hasattr(agent, 'sequence'):
        assert len(agent.sequence) == 3
    else:
        # Detailed failure message if 'sequence' is not found
        params = dir(agent)
        pytest.fail(f"Could not find 'sequence' list. Available attributes: {params}")

def test_tools_assignment():
    """Verify the Strategist agent has the custom SaveBriefTool."""
    agent = build_orchestrator()
    
    # Access the list via 'sequence'
    if hasattr(agent, 'sequence'):
        agents_list = agent.sequence
    else:
        pytest.fail("Cannot find agent list (checked 'sequence').")

    # Access the strategist (2nd agent in sequence)
    strategist = agents_list[1]
    
    assert strategist.tools is not None
    
    # Check if our tool is present
    has_save_tool = False
    for tool in strategist.tools:
        if tool.fn.__name__ == 'save_content_brief_to_state':
            has_save_tool = True
            break
            
    assert has_save_tool, "Strategist agent should have the save_brief tool assigned."
