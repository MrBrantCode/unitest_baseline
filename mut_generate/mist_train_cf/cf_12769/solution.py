"""
QUESTION:
Write a function named `parse_json` that takes a JSON string as input and returns a Python object (such as a dictionary or list) representing the JSON data. The function should be able to handle both simple and complex JSON structures, including nested objects and arrays. Provide a working example of how to access nested elements in the returned Python object. 

The input JSON string will be a valid JSON-formatted string. The function should not perform any error handling for invalid JSON inputs.
"""

import json

def parse_json(json_str):
    """
    Parse a JSON string into a Python object.

    Args:
        json_str (str): A valid JSON-formatted string.

    Returns:
        A Python object (dict or list) representing the JSON data.
    """
    return json.loads(json_str)