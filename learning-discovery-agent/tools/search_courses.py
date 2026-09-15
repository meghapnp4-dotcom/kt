from strands import tool
from utils.catalog import search_catalog


@tool
def search_courses(
    query: str,
    learning_type: str = None,
    provider: str = None,
    level: str = None,
    max_duration_hours: float = None,
):
    """
    Search the learning catalog using keywords and optional filters.
    Returns the highest ranked published courses.
    """

    return search_catalog(
        query=query,
        learning_type=learning_type,
        provider=provider,
        level=level,
        max_duration_hours=max_duration_hours,
    )