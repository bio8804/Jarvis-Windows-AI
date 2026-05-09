import os
from dotenv import load_dotenv

load_dotenv()

# API keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
# GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Settings
WAKE_WORD = "jarvis"
VOICE_RATE = 180
VOICE_VOLUME = 1.0

# Paths
LOG_FILE = "jarvis.log"