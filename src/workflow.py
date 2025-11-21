# --- ROBUST IMPORT BLOCK ---
try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    try:
        from google.adk.agents import SequentialAgent
    except ImportError:
        raise ImportError("Could not find SequentialAgent. Ensure 'google-adk' is installed.")

from src.agents import research_agent, strategist_agent, generator_agent

def build_orchestrator():
    """
    Constructs and returns the main Orchestrator Agent.
    """
    return SequentialAgent(
        name='OmniChannel_Strategist_Orchestrator',
        description='Manages the end-to-end process: research, strategy, and content drafting.',
        # --- THE FINAL FIX IS HERE ---
        sub_agents=[
            research_agent,        # Step 1: Research
            strategist_agent,      # Step 2: Strategy & DB Save
            generator_agent        # Step 3: Final Drafting
        ]
    )
