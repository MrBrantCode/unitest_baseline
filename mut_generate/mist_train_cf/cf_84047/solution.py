"""
QUESTION:
Write a function named `extract_info` that takes a JSON string as input and returns the extracted 'name', 'age', and 'address' values. The input JSON string will be in the format {"name": string, "age": integer, "address": string}. The function should use the built-in Python `json` module to parse the JSON string and extract the required information.
"""

import json

def extract_info(json_string):
    """
    Extract 'name', 'age', and 'address' values from a JSON string.

    Args:
    json_string (str): A JSON string containing 'name', 'age', and 'address' keys.

    Returns:
    dict: A dictionary containing the extracted 'name', 'age', and 'address' values.
    """
    data = json.loads(json_string)
    return {'name': data['name'], 'age': data['age'], 'address': data['address']}