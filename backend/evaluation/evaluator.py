def evaluate_response(output: str):

    score = 0

    length = len(output.split())

    if length > 50:
        score += 4

    if "```" in output:
        score += 3

    if "." in output:
        score += 2

    if length > 150:
        score += 1

    return min(score, 10)
