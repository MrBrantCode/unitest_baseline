"""
QUESTION:
Write a function called `convert_to_json` that uses the `json` module in Python to convert a list of strings representing numbers into a JSON string representation, with each string in the correct numerical format. The input list will only contain strings of decimal numbers. The function should return a JSON string representation of the input list with each string converted to a float.
"""

import json

def convert_to_json(string_list):
    """
    Convert a list of strings representing decimal numbers into a JSON string representation.
    
    Args:
        string_list (list): A list of strings, where each string represents a decimal number.
    
    Returns:
        str: A JSON string representation of the input list with each string converted to a float.
    """
    return json.dumps([float(num) for num in string_list])