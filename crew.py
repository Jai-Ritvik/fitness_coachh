import os
from agents import generate_plan
from utils import save_to_file


class FitnessCoachCrew:
    """
    FitnessCoachCrew:
    - Accepts user inputs (goal, fitness level)
    - Calls the AI agent (OpenRouter) to generate the fitness plan
    - Saves the output to output/fitness_plan.md
    """

    def __init__(self):
        print("⚙️  Initializing Fitness Coach Crew...")

    def run(self, goal: str, level: str) -> str:
        print("\n🤖 Generating your custom fitness plan via OpenRouter...")

        # Call OpenRouter agent — returns plain text string
        plan_text = generate_plan(goal, level)

        # Ensure output folder exists
        os.makedirs("output", exist_ok=True)

        # Save to file
        filepath = save_to_file(content=plan_text, filename="fitness_plan.md")

        return filepath
