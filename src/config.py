import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration Constants
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")

# Use 'gemini-1.5-flash' for speed/cost or 'gemini-1.5-pro' for complex reasoning
MODEL_NAME = 'gemini-1.5-flash'
