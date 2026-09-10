import os
import time
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# User Input
user_input = input("Enter your travel request: ")

# Agent Loop
tasks = [
    "Places to Visit",
    "Accommodation Suggestions",
    "Transportation Options",
    "Food Recommendations",
    "Day-wise Itinerary"
]

for task in tasks:
    print(f"\n🤖 Agent working on {task}...")
    time.sleep(1)

# Prompt
prompt = f"""
You are a Travel Planner Agent.

User Request:
{user_input}

Create a detailed travel plan.

Include:

1. Places to Visit
2. Accommodation Suggestions
3. Transportation Options
4. Food Recommendations
5. Day-wise Itinerary

Make sure the plan stays within the given budget.

Format the answer clearly using headings and bullet points.
"""

print("\n🚀 Generating Final Travel Plan...\n")

# Gemini Response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Streaming Output
for char in response.text:
    print(char, end="", flush=True)
    time.sleep(0.005)

print()