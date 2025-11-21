import pytest
from src.workflow import build_orchestrator

# 1. Import the class directly so we can inspect it
try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    from google.adk.agents import SequentialAgent

def test_reveal_schema():
    """
    THIS TEST IS DESIGNED TO FAIL.
    It extracts the valid field names from the library and prints them 
    inside the error message so we can see them in the logs.
    """
    valid_fields = "UNKNOWN"
    
    try:
        # Attempt to get Pydantic V2 fields
        if hasattr(SequentialAgent, 'model_fields'):
            valid_fields = list(SequentialAgent.model_fields.keys())
        # Attempt to get Pydantic V1 fields
        elif hasattr(SequentialAgent, '__fields__'):
            valid_fields = list(SequentialAgent.__fields__.keys())
        else:
            # Fallback: Get init arguments
            import inspect
            valid_fields = str(inspect.signature(SequentialAgent.__init__))
    except Exception as e:
        valid_fields = f"Error inspecting: {e}"

    # CRASH ON PURPOSE WITH THE ANSWER
    pytest.fail(f"\n\n>>> STOP! HERE IS THE ANSWER: The valid parameters are: {valid_fields} <<<\n")

def test_orchestrator_structure():
    # This will likely fail, but we only care about the test above.
    agent = build_orchestrator()
    assert agent is not None
