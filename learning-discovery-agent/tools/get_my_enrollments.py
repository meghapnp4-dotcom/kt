from strands import tool
from utils.store import load_enrollments


@tool
def get_my_enrollments():
    """
    Return all learner enrollments.
    """

    return load_enrollments()