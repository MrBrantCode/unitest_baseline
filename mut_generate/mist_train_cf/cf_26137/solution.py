"""
QUESTION:
Write a function `convert_to_json` that takes a list of dictionaries as input and returns the JSON representation of the list. The input list contains dictionaries with string keys and values that can be either strings or integers. The function should return a JSON-formatted string that maintains the structure and data types of the input list.
"""

import json

def convert_to_json(data):
    """
    Converts a list of dictionaries into a JSON-formatted string.

    Args:
        data (list): A list of dictionaries with string keys and values that can be either strings or integers.

    Returns:
        str: A JSON-formatted string representing the input list.
    """
    return json.dumps(data)