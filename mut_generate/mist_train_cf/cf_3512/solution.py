"""
QUESTION:
Create a function called `validate_json` that takes a JSON string as input. The function should validate the JSON object and return True if it meets the following conditions, and False otherwise: 
- The JSON object contains the fields "name", "age", "city", and "hobbies".
- The "name" field is a string with a length between 5 and 20 characters.
- The "age" field is an integer greater than or equal to 21.
- The "city" field is one of the following: "New York", "Los Angeles", "Chicago", or "San Francisco".
- The "hobbies" field is a list of strings, each containing at least 3 characters and consisting only of alphabets and spaces.
"""

import json
import re

def validate_json(json_string):
    """
    Validate a JSON string against specific requirements.

    Args:
    json_string (str): The JSON string to validate.

    Returns:
    bool: True if the JSON object is valid, False otherwise.
    """
    
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        return False

    # Check if all required fields are present
    required_fields = ["name", "age", "city", "hobbies"]
    if not all(field in data for field in required_fields):
        return False

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

    return True