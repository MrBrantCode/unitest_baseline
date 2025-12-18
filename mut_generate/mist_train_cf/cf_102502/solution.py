"""
QUESTION:
Write a function `calculate_average_age` that takes a valid JSON string representing a collection of people as input. The JSON string contains a list of people, each with a name, age, and address (street, city, and state). Calculate the average age of people living on the same street and in the same city, and return a dictionary where the keys are tuples of street and city, and the values are the corresponding average ages. Assume that the input JSON string is a valid JSON format.
"""

import json

def calculate_average_age(json_string):
    """
    Calculate the average age of people living on the same street and in the same city.

    Args:
        json_string (str): A valid JSON string representing a collection of people.

    Returns:
        dict: A dictionary where the keys are tuples of street and city, and the values are the corresponding average ages.
    """
    data = json.loads(json_string)
    street_city_ages = {}

    for person in data["People"]:
        street = person["Address"]["Street"]
        city = person["Address"]["City"]
        age = person["Age"]
        
        if (street, city) in street_city_ages:
            street_city_ages[(street, city)]["total_age"] += age
            street_city_ages[(street, city)]["count"] += 1
        else:
            street_city_ages[(street, city)] = {
                "total_age": age,
                "count": 1
            }

    average_ages = {}
    for key in street_city_ages:
        total_age = street_city_ages[key]["total_age"]
        count = street_city_ages[key]["count"]
        average_age = total_age / count
        average_ages[key] = average_age

    return average_ages