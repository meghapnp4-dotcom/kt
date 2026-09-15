# utils/catalog.py

import json
from rank_bm25 import BM25Okapi

CATALOG_FILE = "data/catalog.json"


def load_catalog():
    """
    Load catalog from JSON file.
    """

    try:
        with open(CATALOG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def get_course_by_id(learning_id: str):
    """
    Get a course using its learning ID.
    """

    courses = load_catalog()

    for course in courses:
        if course["learningId"] == learning_id:
            return course

    return None


def search_catalog(
    query: str,
    learning_type: str | None = None,
    provider: str | None = None,
    level: str | None = None,
    max_duration_hours: float | None = None,
):
    """
    Search catalog using BM25 ranking.

    Filters are strict.
    Text relevance is ranked using title,
    description, skills and tags.
    """

    courses = load_catalog()

    # Never show unpublished content
    courses = [
        course
        for course in courses
        if course.get("publishedStatus", False)
    ]

    # Strict filters
    if learning_type:
        courses = [
            course
            for course in courses
            if course["learningType"].lower()
            == learning_type.lower()
        ]

    if provider:
        courses = [
            course
            for course in courses
            if course["provider"].lower()
            == provider.lower()
        ]

    if level:
        courses = [
            course
            for course in courses
            if course["level"].lower()
            == level.lower()
        ]

    if max_duration_hours is not None:
        courses = [
            course
            for course in courses
            if course["durationHours"]
            <= max_duration_hours
        ]

    if not courses:
        return []

    # Build weighted search documents
    documents = []

    for course in courses:

        title = (
            (course.get("title", "") + " ")
            * 4
        )

        description = (
            (course.get("description", "") + " ")
            * 2
        )

        skills = " ".join(
            course.get("skills", [])
        )

        tags = " ".join(
            course.get("tags", [])
        )

        searchable_text = (
            title
            + description
            + skills
            + " "
            + tags
        )

        documents.append(
            searchable_text.lower().split()
        )

    bm25 = BM25Okapi(documents)

    query_tokens = query.lower().split()

    scores = bm25.get_scores(query_tokens)

    ranked_results = sorted(
        zip(courses, scores),
        key=lambda item: item[1],
        reverse=True,
    )

    # Remove duplicates
    seen = set()
    results = []

    for course, score in ranked_results:

        learning_id = course["learningId"]

        if learning_id not in seen:
            seen.add(learning_id)
            results.append(course)

    return results[:30]


def get_popular_courses(
    learning_type: str | None = None,
):
    """
    Return most popular courses ranked by:
    enrollmentCount + rating
    """

    courses = load_catalog()

    courses = [
        course
        for course in courses
        if course.get("publishedStatus", False)
    ]

    if learning_type:
        courses = [
            course
            for course in courses
            if course["learningType"].lower()
            == learning_type.lower()
        ]

    courses.sort(
        key=lambda course: (
            course.get("enrollmentCount", 0),
            course.get("rating", 0),
        ),
        reverse=True,
    )

    return courses[:10]