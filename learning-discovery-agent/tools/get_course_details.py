from strands import tool
from utils.catalog import get_course_by_id


@tool
def get_course_details(learning_id: str):
    """
    Retrieve complete details for a course using learning ID.
    """

    return get_course_by_id(learning_id)