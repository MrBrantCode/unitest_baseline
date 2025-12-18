"""
QUESTION:
Define a function `validate_json` that takes a JSON object as input and validates its contents. The JSON object should contain the following fields: "name", "age", "city", and "hobbies". The validation rules are as follows: "name" is a string with a length between 5 and 20 characters, "age" is an integer greater than or equal to 21, "city" is one of "New York", "Los Angeles", "Chicago", or "San Francisco", and "hobbies" is a list of strings, each containing at least 3 characters and no special characters or numbers. The function should return a boolean indicating whether the JSON object is valid according to these rules.
"""

import json
import re

def validate_json(data):
    """
    Validates a JSON object containing "name", "age", "city", and "hobbies" fields.

    Args:
        data (dict): The JSON object to validate.

    Returns:
        bool: True if the JSON object is valid, False otherwise.
    """

    # Validate the "name" field
    name = data.get("name")
    if not isinstance(name, str) or not 5 <= len(name) <= 20:
        return False

    # Validate the "age" field
    age = data.get("age")
    if not isinstance(age, int) or age < 21:
        return False

    # Validate the "city" field
    city = data.get("city")
    valid_cities = ["New York", "Los Angeles", "Chicago", "San Francisco"]
    if city not in valid_cities:
        return False

    # Validate the "hobbies" field
    hobbies = data.get("hobbies")
    if not isinstance(hobbies, list):
        return False
    else:
        for hobby in hobbies:
            if not isinstance(hobby, str) or len(hobby) < 3 or re.search(r'[^a-zA-Z\s]', hobby):
                return False

    # If all validations pass, return True
    return True