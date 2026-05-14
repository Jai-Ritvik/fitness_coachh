from crew import FitnessCoachCrew

print("🏋️  Welcome to your OpenRouter-Powered Fitness Coach!\n")
goal = input("Enter your fitness goal:\n> ")
level = input("Enter your fitness level (beginner/intermediate/advanced):\n> ")

crew = FitnessCoachCrew()
result_path = crew.run(goal, level)

print("\n" + "=" * 60)
print("🎯 YOUR FITNESS PLAN IS READY!")
print("=" * 60)
print(f"Check your file here: {result_path}")
