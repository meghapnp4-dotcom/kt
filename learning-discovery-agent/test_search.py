from utils.catalog import search_catalog

results = search_catalog("machine learning")

print(f"Results Found: {len(results)}")

for course in results[:5]:
    print(
        course["learningId"],
        course["title"]
    )