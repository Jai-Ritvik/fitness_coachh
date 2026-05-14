# 🏋️ AI Fitness Coach (OpenRouter)

Generate personalized fitness plans using OpenRouter AI via a Flask web app or CLI.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API key
Edit `.env` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
Get your key at: https://openrouter.ai/keys

### 3. (Optional) Change the model
In `agents.py`, update the `MODEL` variable to any OpenRouter-supported model:
```python
MODEL = "openai/gpt-4o-mini"        # fast & cheap
MODEL = "anthropic/claude-3-haiku"  # alternative
```

## Run (Web App)
```bash
python app.py
```
Visit http://127.0.0.1:5000

## Run (CLI)
```bash
python main.py
```

## Project Structure
```
fitness_coach/
├── .env                  # OpenRouter API key
├── app.py                # Flask web app
├── main.py               # CLI entry point
├── crew.py               # Orchestration layer
├── agents.py             # OpenRouter API calls
├── prompts.py            # Prompt templates
├── utils.py              # File save helper
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    ├── style.css
    └── script.js
```
