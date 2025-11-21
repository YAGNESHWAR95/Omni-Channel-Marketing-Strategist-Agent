import json

try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    from google.adk.agents import SequentialAgent

print("\n========== DEBUG: SequentialAgent Schema ==========")
print(json.dumps(SequentialAgent.model_json_schema(), indent=2))
print("===================================================\n")
