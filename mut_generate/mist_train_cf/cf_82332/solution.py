"""
QUESTION:
Create a function named `is_valid_json` that takes a string `data` as input and returns a boolean value indicating whether the string contains valid JSON data. The function should handle nested JSON structures. The input string is expected to use double quotes for keys and values, as per the JSON standard.
"""

import json

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False