import json

print("\n=== DEBUG: SequentialAgent Schema ===")

try:
    from google.adk.agents.workflow import SequentialAgent
except ImportError:
    from google.adk.agents import SequentialAgent

try:
    schema = SequentialAgent.model_json_schema()
    print(json.dumps(schema, indent=2))
except Exception as e:
    print("Failed to fetch schema:", e)

print("=== END DEBUG SCHEMA ===\n")
