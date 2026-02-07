MODEL_PRICING = {
    "gpt-4o": 0.01,
    "mistral-large": 0.006,
    "ollama": 0.0
}


def estimate_cost(model: str, tokens: int):

    price_per_1k = MODEL_PRICING.get(model, 0.005)

    cost = (tokens / 1000) * price_per_1k
    return round(cost, 5)
