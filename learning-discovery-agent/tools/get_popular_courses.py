from strands import tool
from utils.catalog import get_popular_courses


@tool
def get_popular_courses_tool(
    learning_type: str = None,
):
    """
    Return popular learning items ranked by enrollments and rating.
    """

    return get_popular_courses(learning_type)