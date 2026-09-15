from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "API Running"}


@app.get("/courses")
def get_courses():
    with open("data/catalog.json", "r") as f:
        return json.load(f)


@app.get("/popular")
def get_popular():
    with open("data/catalog.json", "r") as f:
        courses = json.load(f)

    courses.sort(
        key=lambda x: x["enrollmentCount"],
        reverse=True
    )

    return courses[:10]