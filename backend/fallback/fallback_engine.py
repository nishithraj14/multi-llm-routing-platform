FALLBACK_ORDER = ["openai", "mistral", "ollama"]


def get_fallback_model(current):

    idx = FALLBACK_ORDER.index(current)

    if idx + 1 < len(FALLBACK_ORDER):
        return FALLBACK_ORDER[idx + 1]

    return None
