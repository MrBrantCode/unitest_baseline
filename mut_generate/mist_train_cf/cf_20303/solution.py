"""
QUESTION:
Write a function called `parse_json` to parse a given JSON string into a Python object and return the object.
"""

import json

def parse_json(json_string):
    """
    Parse a given JSON string into a Python object.

    Args:
        json_string (str): The JSON string to be parsed.

    Returns:
        object: The parsed Python object.
    """
    return json.loads(json_string)