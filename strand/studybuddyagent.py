from strands import Agent
import random

def get_study_tip():
    tips = [
        "Use the Pomodoro technique.",
        "Practice coding every day.",
        "Review notes before sleeping.",
        "Take short breaks while studying.",
        "Focus on one concept at a time."
    ]
    return random.choice(tips)

agent = Agent(
    system_prompt="""
    You are a Study Buddy Agent.
    Help students with study related guidance.

    When somebody asks for a study tip,
    provide one helpful study tip.
    """
)

print("----- Study Buddy Agent -----")

print("\nResponse 1:")
print(get_study_tip())

print("\nResponse 2:")
print("12 * 8 =", 12 * 8)