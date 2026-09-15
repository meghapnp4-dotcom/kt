import json

FILE_PATH = "data/enrollments.json"


def load_enrollments():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except Exception:
        return {"enrollments": []}


def save_enrollments(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)


def enroll(learning_id):
    data = load_enrollments()

    if learning_id in data["enrollments"]:
        return False

    data["enrollments"].append(learning_id)
    save_enrollments(data)

    return True


def unenroll(learning_id):
    data = load_enrollments()

    if learning_id not in data["enrollments"]:
        return False

    data["enrollments"].remove(learning_id)

    save_enrollments(data)

    return True