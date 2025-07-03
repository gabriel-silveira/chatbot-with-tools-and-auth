"""Configuration module that loads environment variables from .env file."""
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Import variables from .env file
from dotenv import dotenv_values
config = dotenv_values(env_path)

# Export variables
ARCADE_API_KEY = config.get('ARCADE_API_KEY', '')
OPENAI_API_KEY = config.get('OPENAI_API_KEY', '')
