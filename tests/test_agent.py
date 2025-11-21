import pytest
from src.workflow import build_orchestrator

def test_orchestrator_structure():
    """Verify the orchestrator is built correctly."""
    agent = build_orchestrator()
    
    # Check the 'sub_agents' property
    assert hasattr(agent, 'sub_agents'), "Orchestrator missing 'sub_agents' property"
    assert len(agent.sub_agents) == 3
    assert agent.name == 'OmniChannel_Strategist_Orchestrator'

def test_tools_assignment():
    """Verify the Strategist agent has the custom SaveBriefTool."""
    agent = build_orchestrator()
    
    # Access the strategist (2nd agent in the list)
    strategist = agent.sub_agents[1]
    
    # Verify tool assignment
    assert strategist.tools is not None
    
    # Check if our tool is present
    has_save_tool = False
    for tool in strategist.tools:
        # FIX: Check tool.name directly instead of tool.fn.__name__
        # The ADK automatically sets the tool name to the function name
        if tool.name == 'save_content_brief_to_state':
            has_save_tool = True
            break
            
    assert has_save_tool, "Strategist agent should have the save_brief tool assigned."
