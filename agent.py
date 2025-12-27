import os
import openai


class SimpleAIAgent:
    """A minimal wrapper around OpenAI ChatCompletion.

    Configure the API key with the `OPENAI_API_KEY` environment variable.
    """

    def __init__(self, api_key: str | None = None, model: str = "gpt-4o-mini"):
        if api_key:
            openai.api_key = api_key
        else:
            # allow default env var
            openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model

    def ask(self, prompt: str) -> str:
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
        )
        return resp.choices[0].message.content.strip()
