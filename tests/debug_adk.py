import sys
import os

# Add src to path just in case, though not strictly needed for this test
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Try importing from the location that worked in your logs
    from google.adk.agents.workflow import SequentialAgent
    print(f"\nSUCCESS: Imported SequentialAgent from google.adk.agents.workflow")
except ImportError:
    try:
        from google.adk.agents import SequentialAgent
        print(f"\nSUCCESS: Imported SequentialAgent from google.adk.agents")
    except ImportError:
        print("\nCRITICAL ERROR: Could not import SequentialAgent.")
        sys.exit(1)

print("-" * 40)
print("INSPECTING SequentialAgent EXPECTED FIELDS")
print("-" * 40)

# 1. Check Pydantic Fields (Most likely answer)
if hasattr(SequentialAgent, 'model_fields'):
    print(f"Valid Pydantic Fields: {list(SequentialAgent.model_fields.keys())}")
else:
    print("Not a standard Pydantic v2 model.")

# 2. Check Constructor (Fallback)
import inspect
sig = inspect.signature(SequentialAgent.__init__)
print(f"Constructor Arguments: {sig}")
