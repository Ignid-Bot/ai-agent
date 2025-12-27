import types
import pytest

from agent import SimpleAIAgent

class DummyResp:
    def __init__(self, text):
        self.choices = [types.SimpleNamespace(message=types.SimpleNamespace(content=text))]


def test_ask_returns_text(monkeypatch):
    def fake_create(*args, **kwargs):
        return DummyResp("hello from fake")

    import openai
    monkeypatch.setattr(openai.ChatCompletion, "create", fake_create)

    agent = SimpleAIAgent(api_key="test")
    resp = agent.ask("hi")
    assert isinstance(resp, str)
    assert "hello" in resp
