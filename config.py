import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AI_PROVIDER = os.getenv('AI_PROVIDER', 'deepseek')

WAKE_WORD = 'jarvis'
VOICE_RATE = 180
VOICE_VOLUME = 1.0

LOG_FILE = 'jarvis.log'
