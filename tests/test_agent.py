import pytest
import sys
from src.workflow import build_orchestrator

# Import the class directly to inspect it
try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    from google.adk.agents import SequentialAgent

def test_debug_agent_schema():
    """
    CRITICAL DEBUG TEST:
    This test inspects the SequentialAgent class and PRINTS the valid arguments 
    to the console so we can stop guessing.
    """
    print("\n" + "="*60)
    print("🔎 INSPECTING SEQUENTIAL AGENT SCHEMA")
    print("="*60)
    
    try:
        # Check Pydantic V2 fields
        if hasattr(SequentialAgent, 'model_fields'):
            keys = list(SequentialAgent.model_fields.keys())
            print(f"✅ VALID PARAMS FOUND: {keys}")
        # Check Pydantic V1 fields
        elif hasattr(SequentialAgent, '__fields__'):
            keys = list(SequentialAgent.__fields__.keys())
            print(f"✅ VALID PARAMS FOUND: {keys}")
        else:
            print("❌ Could not find Pydantic fields. Checking __init__...")
            import inspect
            print(inspect.signature(SequentialAgent.__init__))
            
    except Exception as e:
        print(f"❌ Error during inspection: {e}")

    print("="*60 + "\n")
    
    # We force a pass here so we can see the output even if other tests fail
    assert True

def test_orchestrator_structure():
    agent = build_orchestrator()
    # Check 'sequence'
    assert len(agent.sequence) == 3
