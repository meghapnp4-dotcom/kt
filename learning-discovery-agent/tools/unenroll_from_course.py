from strands import tool
from utils.store import unenroll


@tool
def unenroll_from_course(learning_id: str):
    """
    Remove a learner enrollment.
    """

    return unenroll(learning_id)