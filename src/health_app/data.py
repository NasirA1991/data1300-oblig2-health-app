import json
from health_app.health import Health
from collections import Counter


def save(records, file="health_records.json"):
    data = []
    for record in records:
        item = {
            "name": record.name,
            "weight_kg": record.weight_kg,
            "height_m": record.height_m,
            "calculated_bmi": record.calculate_bmi()
        }
        data.append(item)

    with open(file, "w") as f:
        json.dump(data, f, indent=2)


def read(file="health_records.json"):
    try:
        with open(file, "r") as f:
            data = json.load(f)
            people = []

            for person in data:
                record = Health(
                    person["name"],
                    person["weight_kg"],
                    person["height_m"]
                )
                people.append(record)
            return people
    except FileNotFoundError:
        return []

def get_statistics(file="health_records.json") -> dict:
    records = read(file)
    total_records = len(records)
    bmi_cumulative = 0
    categories = []

    for person in records:
        bmi_cumulative += person.calculate_bmi()
        categories.append(person.category_bmi())

    avg_bmi = round((bmi_cumulative / total_records), 2)
    category_distribution = Counter(categories)
    most_common_category = category_distribution.most_common(1)[0][0]


    return {
        "total_records": total_records,
        "avg_bmi": avg_bmi,
        "most_common_category": most_common_category,
        "category_distribution": category_distribution
    }



