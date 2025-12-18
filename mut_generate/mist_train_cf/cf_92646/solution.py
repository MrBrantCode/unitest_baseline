"""
QUESTION:
Create a function called `get_name` that takes a JSON string as input and returns the value of the "name" property within the "person" object. The JSON string has a nested structure with objects and arrays, but only the "name" property within the "person" object needs to be accessed. The function should use the json.loads method to parse the JSON string into a Python dictionary.
"""

import json

def get_name(json_string):
    """
    This function takes a JSON string as input, parses it into a Python dictionary, 
    and returns the value of the "name" property within the "person" object.

    Args:
        json_string (str): A JSON string with a nested structure.

    Returns:
        str: The value of the "name" property within the "person" object.
    """
    data = json.loads(json_string)
    person = data.get("person", {})
    return person.get("name")