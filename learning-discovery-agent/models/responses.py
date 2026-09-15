from typing import Literal
from pydantic import BaseModel, Field


class LearningResponse(BaseModel):
    type: Literal[
        "search",
        "enroll",
        "enrolled",
        "enrollment_list",
        "unenroll",
        "unenrolled",
        "answer",
    ]

    title: str = Field(
        description="Short title for the response"
    )

    learning_ids: list[str] = Field(
        default_factory=list
    )

    message: str = Field(
        description="Main user-facing response"
    )

    next_step_questions: list[str] = Field(
        default_factory=list
    )