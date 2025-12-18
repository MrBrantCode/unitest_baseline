"""
QUESTION:
Convert a JSON string to a dictionary with only the "name", "age", and "city" keys. The function should take a JSON string as input, where the "name" and "city" values are strings and the "age" value is an integer. The function should ignore any additional key-value pairs in the JSON string.
"""

import json

def extract_required_keys(json_string):
    """
    Convert a JSON string to a dictionary with only the "name", "age", and "city" keys.

    Args:
        json_string (str): A JSON string containing the "name", "age", and "city" keys.

    Returns:
        dict: A dictionary containing the required keys ("name", "age", and "city") and their values.
    """
    data = json.loads(json_string)
    required_keys = ["name", "age", "city"]
    return {key: data[key] for key in required_keys if key in data}