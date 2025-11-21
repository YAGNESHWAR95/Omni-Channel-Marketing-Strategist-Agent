import sys
import os

# Ensure the src module is found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.workflow import build_orchestrator

def main():
    print("--- Omni-Channel Marketing Strategist Agent ---")
    print("Initializing Agents...")
    
    orchestrator = build_orchestrator()
    
    # Interactive loop
    try:
        user_goal = input("\nEnter your marketing goal (e.g., 'Promote our new eco-friendly coffee cup'): ")
        if user_goal.strip():
            print(f"\n[Orchestrator] Received goal. Starting workflow for: {user_goal}...\n")
            result = orchestrator.invoke(user_goal)
            print("\n" + "="*50)
            print("FINAL RESULT")
            print("="*50)
            print(result)
        else:
            print("No goal entered. Exiting.")
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
