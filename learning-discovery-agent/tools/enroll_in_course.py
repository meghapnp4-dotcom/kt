from strands import tool
from utils.store import enroll


@tool
def enroll_in_course(learning_id: str):
    """
    Enroll the learner into a course.
    """

    return enroll(learning_id)