"""
QUESTION:
Create a function named `generate_json_object` that takes a dictionary as input and returns its equivalent JSON object as a string.
"""

import json

def generate_json_object(input_dict):
    """
    This function takes a dictionary as input and returns its equivalent JSON object as a string.

    Args:
        input_dict (dict): The dictionary to be converted into a JSON object.

    Returns:
        str: The JSON object as a string.
    """
    return json.dumps(input_dict)