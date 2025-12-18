"""
QUESTION:
Write a function named `convert_json_to_dict` that takes a JSON string containing nested objects and arrays as input and returns a valid Python dictionary. The input JSON string can have multiple levels of nesting.
"""

import json

def convert_json_to_dict(json_string):
    """
    Converts a JSON string into a valid Python dictionary.
    
    Args:
        json_string (str): The input JSON string containing nested objects and arrays.
    
    Returns:
        dict: A valid Python dictionary representation of the input JSON string.
    """
    return json.loads(json_string)