from litellm import completion


def call_mistral(prompt: str):

    response = completion(
        model="mistral-large",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content
    tokens = response.usage.total_tokens

    return output, tokens
