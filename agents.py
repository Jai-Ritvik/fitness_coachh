import os
import requests
from prompts import PLAN_PROMPT, DAILY_WORKOUT_PROMPT
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")
print(f"API KEY: {'set' if api_key else 'NOT FOUND - check your .env file'}")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-4o-mini"  # Change to any OpenRouter-supported model


def _call_openrouter(prompt: str) -> str:
    """Send a prompt to OpenRouter and return the response text."""
    if not api_key:
        raise ValueError("ERROR: OPENROUTER_API_KEY not found in .env file!")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise RuntimeError(
            f"OpenRouter API error {response.status_code}: {response.text}"
        )

    data = response.json()
    return data["choices"][0]["message"]["content"]


def generate_plan(goal: str, level: str = "beginner") -> str:
    """Generate a full weekly fitness plan."""
    prompt = PLAN_PROMPT.format(goal=goal, level=level)
    return _call_openrouter(prompt)


def generate_daily_workout(level: str) -> str:
    """Generate a single day's workout."""
    prompt = DAILY_WORKOUT_PROMPT.format(level=level)
    return _call_openrouter(prompt)
