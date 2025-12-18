"""
QUESTION:
Write a function named `parse_nested_json` that takes a string representing a nested JSON object as input and returns a dictionary containing the parsed data. The input JSON object can contain arrays and objects. The function should be implemented in Python and utilize the `json` module.
"""

import json

def parse_nested_json(json_str):
    """
    This function takes a string representing a nested JSON object as input and returns a dictionary containing the parsed data.

    Args:
        json_str (str): A string representing a nested JSON object.

    Returns:
        dict: A dictionary containing the parsed data.
    """
    return json.loads(json_str)