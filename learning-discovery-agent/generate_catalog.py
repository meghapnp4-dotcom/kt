import json

courses = []

providers = ["Cognizant", "MS Learn", "Skillsoft", "AWS Builder"]
levels = ["beginner", "intermediate", "advanced"]

topics = [
    "Machine Learning",
    "Python",
    "AWS",
    "Data Engineering",
    "DevOps",
    "Generative AI",
    "Java",
    "React",
    "Docker",
    "Kubernetes"
]

for i in range(1, 51):
    topic = topics[(i - 1) % len(topics)]

    courses.append({
        "learningId": f"LRN-{i:05d}",
        "title": f"{topic} Fundamentals {i}",
        "description": f"Learn {topic} concepts and practical implementation.",
        "learningType": ["course", "lesson", "concept", "learning path", "program"][i % 5],
        "provider": providers[i % 4],
        "skills": [topic.lower(), "problem solving"],
        "level": levels[i % 3],
        "durationHours": round((i % 8) + 1.5, 1),
        "prerequisiteNames": [],
        "publishedStatus": False if i % 13 == 0 else True,
        "rating": round(3.5 + (i % 15) * 0.1, 1),
        "enrollmentCount": 100 + i * 50,
        "tags": [topic.lower()]
    })

with open("data/catalog.json", "w") as f:
    json.dump(courses, f, indent=2)

print(f"Generated {len(courses)} courses")