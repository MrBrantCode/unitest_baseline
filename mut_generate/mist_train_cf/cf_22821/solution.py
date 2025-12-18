"""
QUESTION:
Write a Python function `convert_to_json` that takes a dictionary as input. The function should add a new key-value pair "email" with a string value between 5 and 50 characters, and validate the existing keys: "firstName" should be a string between 2 and 20 characters, "lastName" should be a string between 2 and 20 characters, and "age" should be an integer between 18 and 100 (inclusive). Return the resulting dictionary in JSON format if all conditions are met; otherwise, return an error message or handle the error accordingly.
"""

import json
import re

def convert_to_json(data):
    """
    Converts a dictionary to JSON format after adding an 'email' key and validating existing keys.

    Args:
        data (dict): The input dictionary.

    Returns:
        str: The resulting dictionary in JSON format if all conditions are met; otherwise, an error message.
    """

    # Add a new key-value pair "email" with a string value between 5 and 50 characters
    data["email"] = "example@example.com"

    # Validate the existing keys
    if (not isinstance(data.get("firstName"), str) or 
        not 2 <= len(data.get("firstName", "")) <= 20 or 
        not isinstance(data.get("lastName"), str) or 
        not 2 <= len(data.get("lastName", "")) <= 20 or 
        not isinstance(data.get("age"), int) or 
        not 18 <= data.get("age", 0) <= 100 or 
        not re.match(r"[^@]+@[^@]+\.[^@]+", data.get("email", ""))):
        return "Error: Input data does not meet the requirements."

    return json.dumps(data)