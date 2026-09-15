import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "gemini")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini/gemini-2.5-flash")