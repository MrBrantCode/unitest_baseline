"""
QUESTION:
Create a function called `extract_nested_dicts` that takes a string as input, where the string represents a nested data structure containing dictionaries, lists, and numbers. The function should convert the string to a Python object, handle exceptions for any type other than dictionaries, lists, and numbers, and return a list of all nested dictionaries.
"""

import json

def extract_nested_dicts(data):
    # Initialize an empty list to store all nested dictionaries
    nested_dicts = []

    # Use recursion to extract all nested dictionaries
    def extract(data):
        # Check if the data is a dictionary
        if isinstance(data, dict):
            nested_dicts.append(data)
            for value in data.values():
                extract(value)
        # Check if the data is a list
        elif isinstance(data, list):
            for value in data:
                extract(value)

    # Convert the string to a Python dictionary
    data = json.loads(data.replace("'",'"'))

    # Call the recursive function
    extract(data)
    return nested_dicts