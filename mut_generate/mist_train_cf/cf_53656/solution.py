"""
QUESTION:
Write a function called `parse_json_to_dict` that takes a string representing a multi-level JSON object as input and returns a structurally corresponding Python dictionary. The function should be able to handle nested JSON objects.
"""

import json

def parse_json_to_dict(json_string):
    """
    This function takes a string representing a multi-level JSON object as input and returns a structurally corresponding Python dictionary.

    Args:
        json_string (str): A string representing a multi-level JSON object.

    Returns:
        dict: A structurally corresponding Python dictionary.
    """
    return json.loads(json_string)