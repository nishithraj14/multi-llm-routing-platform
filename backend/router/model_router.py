def select_model(prompt: str, priority="balanced"):

    prompt_lower = prompt.lower()

    if priority == "quality":
        return "openai"

    if priority == "speed":
        return "mistral"

    if "code" in prompt_lower or "architecture" in prompt_lower:
        return "openai"

    if "summary" in prompt_lower or "fast" in prompt_lower:
        return "mistral"

    return "ollama"
