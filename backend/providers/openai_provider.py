from litellm import completion


def call_openai(prompt: str):

    response = completion(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content
    tokens = response.usage.total_tokens

    return output, tokens
