import requests
from backend.config import OLLAMA_BASE_URL


def call_ollama(prompt: str, model="llama3"):

    url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)

    data = response.json()

    output = data.get("response", "")
    tokens = len(output.split())

    return output, tokens
