"""
QUESTION:
Write a function named `parse_json(json_string)` that takes a JSON string as input and attempts to parse it into a Python dictionary. The function should return the parsed dictionary if the JSON string is valid, and an error message as a string if the JSON string is invalid, contains nested dictionaries or lists, or has missing or invalid keys. The function should handle various data types such as integers, floats, booleans, and null values.
"""

import json

def parse_json(json_string):
    try:
        data = json.loads(json_string)
        if isinstance(data, dict) and not any(isinstance(value, (list, dict)) for value in data.values()):
            return data
        else:
            return "Error: JSON string contains nested dictionaries or lists, or has missing or invalid keys."
    except json.JSONDecodeError as e:
        return str(e)