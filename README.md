# ai-agent

[![Python tests](https://github.com/Ignid-Bot/ai-agent/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Ignid-Bot/ai-agent/actions/workflows/python-tests.yml)

Minimal Python AI agent example (call an LLM via OpenAI API).

## Setup

1. Create a virtual environment and install deps:

```bash
python -m venv .venv
source .venv/bin/activate   # or `.venv\\Scripts\\activate` on Windows
pip install -r requirements.txt
```

2. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="sk-..."    # macOS / Linux
setx OPENAI_API_KEY "sk-..."      # Windows (new shell)
```

3. Run the agent:

```bash
python main.py
```

## Git / push example

If you want to push this repo to GitHub (replace URL with your repo):

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Ignid-Bot/ai-agent.git
git push -u origin main
```

Note: you need Git credentials (PAT) or an authenticated Git client to push.

## Next steps

- Add conversation memory, tools, or task-specific prompts
- Integrate with a framework like LangChain for retrieval
- Add tests and CI
