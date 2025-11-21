# --- ROBUST IMPORT BLOCK ---
# Some versions of ADK put SequentialAgent in .agents, others in .agents.workflow
try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    try:
        from google.adk.agents import SequentialAgent
    except ImportError:
        raise ImportError("Could not find SequentialAgent. Ensure 'google-adk' is installed.")

from src.agents import research_agent, strategist_agent, generator_agent

# ... imports ...

def build_orchestrator():
    return SequentialAgent(
        name='OmniChannel_Strategist_Orchestrator',
        description='...',
        # TRY THIS PARAMETER NAME:
        sequence=[ 
            research_agent,
            strategist_agent,
            generator_agent
        ]
    )
    )
