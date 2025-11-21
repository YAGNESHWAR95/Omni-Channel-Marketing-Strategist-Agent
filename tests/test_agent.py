import pytest
from src.workflow import build_orchestrator

def test_orchestrator_structure():
    """Verify the orchestrator is built correctly."""
    agent = build_orchestrator()
    
    # Check if the 'sequence' attribute exists and has 3 items
    # We use getattr to be safe against naming variations
    if hasattr(agent, 'sequence'):
        assert len(agent.sequence) == 3
    elif hasattr(agent, 'steps'):
        assert len(agent.steps) == 3
    elif hasattr(agent, 'agents'):
        assert len(agent.agents) == 3
    else:
        # Fallback: Fail if we can't find the list
        pytest.fail("Could not find 'sequence', 'steps', or 'agents' list in the Orchestrator.")

def test_tools_assignment():
    """Verify the Strategist agent has the custom SaveBriefTool."""
    agent = build_orchestrator()
    
    # Get the list of agents (handling different property names)
    if hasattr(agent, 'sequence'):
        agents_list = agent.sequence
    elif hasattr(agent, 'steps'):
        agents_list = agent.steps
    else:
        agents_list = agent.agents

    # Access the strategist (2nd agent in sequence)
    strategist = agents_list[1]
    
    # Verify tool assignment
    assert strategist.tools is not None
    
    # Check if our tool is present
    has_save_tool = False
    for tool in strategist.tools:
        if tool.fn.__name__ == 'save_content_brief_to_state':
            has_save_tool = True
            break
            
    assert has_save_tool, "Strategist agent should have the save_brief tool assigned."
