from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(
    filename="agent.log",
    level=logging.ERROR
)

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini/gemini-1.5-flash"
)

from strands import Agent
from strands.models.litellm import LiteLLMModel

from config.prompts import SYSTEM_PROMPT

from tools.search_courses import search_courses
from tools.get_course_details import get_course_details
from tools.enroll_in_course import enroll_in_course
from tools.unenroll_from_course import unenroll_from_course
from tools.get_my_enrollments import get_my_enrollments
from tools.get_popular_courses import get_popular_courses_tool

print(f"Using model: {MODEL_NAME}")

model = LiteLLMModel(
    model_id=MODEL_NAME
)

agent = Agent(
    model=model,
    tools=[
        search_courses,
        get_course_details,
        enroll_in_course,
        unenroll_from_course,
        get_my_enrollments,
        get_popular_courses_tool,
    ],
    system_prompt=SYSTEM_PROMPT,
)

print("Learning Discovery Agent")
print("Type 'exit' to quit")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    try:
        response = agent(user_input)

        print("\nAgent:")
        print(response)

    except Exception as e:
        logging.exception("Agent execution failed")

        print("\nERROR:")
        print(type(e))
        print(e)