"""
QUESTION:
Create a function called `dict_to_json` that converts a Python dictionary into a JSON formatted string. The function should use the `json.dumps()` function to perform the conversion.
"""

import json

def dict_to_json(dictionary):
    """
    Convert a Python dictionary into a JSON formatted string.

    Args:
        dictionary (dict): The dictionary to be converted.

    Returns:
        str: A JSON formatted string representation of the dictionary.
    """
    return json.dumps(dictionary)