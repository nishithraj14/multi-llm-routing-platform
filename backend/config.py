import os
from dotenv import load_dotenv

# Load .env at config import time
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./llm_logs.db")


def validate_keys():

    missing = []

    if not OPENAI_API_KEY:
        missing.append("OPENAI_API_KEY")

    if not MISTRAL_API_KEY:
        missing.append("MISTRAL_API_KEY")

    if missing:
        raise Exception(
            f"Missing environment variables: {', '.join(missing)}"
        )
