"""
QUESTION:
Write a Python function called `parse_json_data` to read and parse JSON data. The function should take a JSON string as input and return the parsed data as a Python object. The function should use the built-in `json` module to parse the JSON data.
"""

import json

def parse_json_data(json_string):
    """
    This function takes a JSON string as input and returns the parsed data as a Python object.
    
    Parameters:
    json_string (str): The JSON string to be parsed.
    
    Returns:
    dict: The parsed JSON data as a Python dictionary.
    """
    return json.loads(json_string)