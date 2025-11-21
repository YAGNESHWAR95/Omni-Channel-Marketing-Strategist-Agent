import pytest
from src.workflow import build_orchestrator
from src.tools import SaveBriefTool

def test_orchestrator_structure():
    """Verify the orchestrator is built with 3 agents."""
    agent = build_orchestrator()
    assert len(agent.agents) == 3
    assert agent.name == 'OmniChannel_Strategist_Orchestrator'

def test_tools_assignment():
    """Verify the Strategist agent has the custom SaveBriefTool."""
    agent = build_orchestrator()
    # Access the strategist (2nd agent in sequence)
    strategist = agent.agents[1]
    
    tool_names = [t.name for t in strategist.tools]
    assert "save_brief" in tool_names

def test_json_cleaner_logic():
    """Test if our tool function correctly strips Markdown."""
    from src.tools import save_content_brief_to_state
    
    # Simulated LLM output with markdown
    mock_input = '```json\n{"topic": "Test", "target_platform": "X"}\n```'
    result = save_content_brief_to_state(mock_input)
    
    assert "SUCCESS" in result
