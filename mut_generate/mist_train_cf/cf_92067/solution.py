"""
QUESTION:
Create a function named `parse_json` that takes a JSON string as input, parses it into a dictionary or equivalent data structure, and returns the parsed data. The JSON string may contain nested arrays and objects.
"""

import json

def parse_json(json_str):
    """
    Parse a JSON string into a dictionary or equivalent data structure.

    Args:
        json_str (str): The JSON string to parse.

    Returns:
        dict: The parsed data.
    """
    return json.loads(json_str)