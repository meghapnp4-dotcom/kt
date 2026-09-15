from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

from strands import Agent
from strands.models.litellm import LiteLLMModel

model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash"
)

agent = Agent(model=model)

response = agent("Say hello in one sentence")

print(response)