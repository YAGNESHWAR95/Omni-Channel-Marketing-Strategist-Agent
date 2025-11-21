# --- ROBUST IMPORT BLOCK ---


# TEMP: Print valid fields for SequentialAgent in CI
try:
    import json
    print("\n========== DEBUG: SequentialAgent Schema ==========")
    print(json.dumps(SequentialAgent.model_json_schema(), indent=2))
    print("===================================================\n")
except Exception as e:
    print("Schema fetch failed:", e)

try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    try:
        from google.adk.agents import SequentialAgent
    except ImportError:
        raise ImportError("Could not find SequentialAgent. Ensure 'google-adk' is installed.")

from src.agents import research_agent, strategist_agent, generator_agent

# DEBUG: Print allowed fields for SequentialAgent in CI logs


def build_orchestrator():
    """
    Constructs and returns the main Orchestrator Agent.
    """
    return SequentialAgent(
        name='OmniChannel_Strategist_Orchestrator',
        description='Manages the end-to-end process: research, strategy, and content drafting.',
        steps=[
            research_agent,        # Step 1: Research
            strategist_agent,      # Step 2: Strategy & DB Save
            generator_agent        # Step 3: Final Drafting
        ]
    )

