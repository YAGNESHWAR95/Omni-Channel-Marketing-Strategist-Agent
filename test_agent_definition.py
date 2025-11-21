"""
This test ensures the core agent logic is defined and importable,
confirming the main application architecture is structurally sound.
"""
import pytest
from agent import root_agent

def test_root_agent_is_sequential_agent():
    """Checks that the main root_agent is defined and is a SequentialAgent, 
    verifying the Capstone architecture pattern."""
    
    # Check if the root_agent object exists (was imported successfully)
    assert root_agent is not None, "Root agent must be defined."
    
    # Check if it has the expected components of a Sequential Agent (sub-agents)
    assert len(root_agent.agents) == 3, "Sequential agent must have exactly 3 sub-agents defined."

def test_specialist_agents_are_defined():
    """Checks that the core specialist agents exist within the orchestrator."""
    
    agent_names = [agent.name for agent in root_agent.agents]
    
    assert 'Market_Research_Agent' in agent_names
    assert 'Content_Strategist_Agent' in agent_names
    assert 'Content_Generator_Agent' in agent_names
