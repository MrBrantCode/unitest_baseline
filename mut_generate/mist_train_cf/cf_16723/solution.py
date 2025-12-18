"""
QUESTION:
Create a function `preprocess_data` that takes a list of dictionaries as input. Each dictionary should have the keys "name", "age", "gender", "city", and "hobbies". The function should return a list of dictionaries with the same length, where each dictionary has the keys "name", "age_group", "gender", "location", and "hobbies". The "age_group" should be determined by the age ranges: 0-5 ("infant"), 6-12 ("child"), 13-19 ("adolescent"), 20-30 ("young adult"), 31-40 ("adult"), 41-50 ("middle-aged adult"), and 51+ ("senior"). The "location" should be determined by the city, with the following mappings: "New York" and "Boston" to "East Coast", "Los Angeles", "San Francisco", and "Seattle" to "West Coast", "Chicago" to "Midwest", "Houston", "Atlanta", and "Dallas" to "South", and all other cities to "Other".
"""

def preprocess_data(input_data):
    age_groups = {
        (0, 5): "infant",
        (6, 12): "child",
        (13, 19): "adolescent",
        (20, 30): "young adult",
        (31, 40): "adult",
        (41, 50): "middle-aged adult"
    }

    locations = {
        "New York": "East Coast",
        "Los Angeles": "West Coast",
        "Chicago": "Midwest",
        "Houston": "South",
        "San Francisco": "West Coast",
        "Seattle": "West Coast",
        "Boston": "East Coast",
        "Atlanta": "South",
        "Dallas": "South"
    }

    output_data = []
    for person in input_data:
        age = person["age"]
        age_group = next((group for (lower, upper), group in age_groups.items() if lower <= age <= upper), "senior")

        city = person["city"]
        location = locations.get(city, "Other")

        output_person = {
            "name": person["name"],
            "age_group": age_group,
            "gender": person["gender"],
            "location": location,
            "hobbies": person["hobbies"]
        }
        output_data.append(output_person)

    return output_data