"""
QUESTION:
Write a function `validate_json_data` that takes a JSON string as input and returns a dictionary with validation results for the "name", "age", "email", and "address" fields. The function should validate that the "name" and "address" fields are non-empty strings, the "age" field is a positive integer, and the "email" field is a valid email address.
"""

import json
import re

def validate_json_data(json_string):
    """
    Validate the given JSON string.

    Args:
    json_string (str): The JSON string to be validated.

    Returns:
    dict: A dictionary with validation results for the "name", "age", "email", and "address" fields.
    """
    # Initialize validation results
    validation_results = {
        "name": False,
        "age": False,
        "email": False,
        "address": False
    }

    try:
        # Parse JSON data
        json_data = json.loads(json_string)

        # Validate name field
        if "name" in json_data and json_data["name"]:
            validation_results["name"] = True

        # Validate age field
        if "age" in json_data and isinstance(json_data["age"], int) and json_data["age"] > 0:
            validation_results["age"] = True

        # Validate email field
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if "email" in json_data and re.match(email_regex, json_data["email"]):
            validation_results["email"] = True

        # Validate address field
        if "address" in json_data and json_data["address"]:
            validation_results["address"] = True

    except json.JSONDecodeError:
        # Handle invalid JSON data
        pass

    return validation_results