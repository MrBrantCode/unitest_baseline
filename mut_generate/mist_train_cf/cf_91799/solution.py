"""
QUESTION:
Write a function named `validate_json` that takes a JSON string as input and validates that it contains a "name" field which is a string, an "age" field which is an integer greater than 18, and a "city" field which is one of the following: "New York", "Los Angeles", or "Chicago".
"""

import json

def validate_json(json_string):
    """
    Validates a JSON string to ensure it contains a "name" field which is a string, 
    an "age" field which is an integer greater than 18, and a "city" field which is 
    one of the following: "New York", "Los Angeles", or "Chicago".

    Args:
        json_string (str): The JSON string to be validated.

    Returns:
        bool: True if the JSON string is valid, False otherwise.
    """

    try:
        # Parse the JSON string
        data = json.loads(json_string)

        # Validate name field
        if not isinstance(data.get('name'), str):
            return False

        # Validate age field
        if not (isinstance(data.get('age'), int) and data.get('age') > 18):
            return False

        # Validate city field
        valid_cities = ["New York", "Los Angeles", "Chicago"]
        if data.get('city') not in valid_cities:
            return False

        return True
    except json.JSONDecodeError:
        return False