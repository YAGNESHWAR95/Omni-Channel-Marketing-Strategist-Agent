# --- ROBUST IMPORT BLOCK ---

# First: safely import SequentialAgent
try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    try:
        from google.adk.agents import SequentialAgent
    except ImportError:
        raise ImportError("Could not find SequentialAgent. Ensure 'google-adk' is installed.")

# Second: NOW we can safely print schema for debugging
try:
    import json
    print("\n========== DEBUG: SequentialAgent Schema ==========")
    print(json.dumps(SequentialAgent.model_json_schema(), indent=2))
    print("===================================================\n")
except Exception as e:
    print("Schema fetch failed:", e)

# Third: import your agents
from src.agents import research_agent, strategist_agent, generator_agent


def build_orchestrator():
    return SequentialAgent(
        name='OmniChannel_Strategist_Orchestrator',
        description='Manages the end-to-end process: research, strategy, and content drafting.',
        steps=[
            research_agent,
            strategist_agent,
            generator_agent
        ]
    )
