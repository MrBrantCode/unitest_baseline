"""
QUESTION:
Write a function `convert_json_to_dict(json_string)` that converts a nested JSON string to its Python dictionary equivalent. The function should take a JSON string as input and return a dictionary. Assume the input JSON string is valid.
"""

import json

def convert_json_to_dict(json_string):
    """
    Converts a nested JSON string to its Python dictionary equivalent.

    Args:
    json_string (str): A valid JSON string.

    Returns:
    dict: A Python dictionary equivalent to the input JSON string.
    """
    return json.loads(json_string)