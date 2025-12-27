#!/usr/bin/env python3
import os
from agent import SimpleAIAgent


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable first.")
        return
    agent = SimpleAIAgent(api_key=api_key)
    print("Simple AI Agent — ketik prompt lalu Enter (kosong untuk keluar)")
    while True:
        prompt = input("> ")
        if not prompt.strip():
            break
        try:
            resp = agent.ask(prompt)
            print("\n--- Response ---\n")
            print(resp)
            print("\n----------------\n")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
