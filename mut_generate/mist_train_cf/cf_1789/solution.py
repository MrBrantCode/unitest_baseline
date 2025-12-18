"""
QUESTION:
Implement a function `preprocess_data` that takes a list of dictionaries representing people's information and returns a modified list of dictionaries. Each person's information should have the following attributes: "name" (string), "age_group" (string), "gender" (string), "location" (string), "hobbies" (list of strings), and "friend_suggestions" (list of strings).

The "age_group" attribute should be based on the person's age, with the following ranges:
- 0-5 years old: "infant"
- 6-12 years old: "child"
- 13-19 years old: "adolescent"
- 20-30 years old: "young adult"
- 31-40 years old: "adult"
- 41-50 years old: "middle-aged adult"
- 51 years old and above: "senior"

The "location" attribute should be based on the person's city, with the following mappings:
- "New York": "East Coast"
- "Los Angeles": "West Coast"
- "Chicago": "Midwest"
- "Houston": "South"
- "San Francisco": "West Coast"
- "Seattle": "West Coast"
- "Boston": "East Coast"
- "Atlanta": "South"
- "Dallas": "South"
- "Other cities": "Other"

The "friend_suggestions" attribute should contain a list of names of people who have at least one hobby in common with the person, meet the following criteria:
- Same gender as the person
- Same age group as the person
- Different location than the person
"""

def preprocess_data(people):
    age_groups = {
        range(0, 6): "infant",
        range(6, 13): "child",
        range(13, 20): "adolescent",
        range(20, 31): "young adult",
        range(31, 41): "adult",
        range(41, 51): "middle-aged adult"
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

    def get_age_group(age):
        for age_range, age_group in age_groups.items():
            if age in age_range:
                return age_group
        return "senior"

    def get_location(city):
        return locations.get(city, "Other")

    def get_friend_suggestions(person, people):
        suggestions = []
        person_age_group = get_age_group(person["age"])
        person_location = get_location(person["city"])
        for other_person in people:
            if other_person != person and \
                other_person["gender"] == person["gender"] and \
                get_age_group(other_person["age"]) == person_age_group and \
                get_location(other_person["city"]) != person_location and \
                any(hobby in other_person["hobbies"] for hobby in person["hobbies"]):
                suggestions.append(other_person["name"])
        return suggestions

    modified_people = []
    for person in people:
        modified_person = {
            "name": person["name"],
            "age_group": get_age_group(person["age"]),
            "gender": person["gender"],
            "location": get_location(person["city"]),
            "hobbies": person["hobbies"],
            "friend_suggestions": get_friend_suggestions(person, people)
        }
        modified_people.append(modified_person)

    return modified_people