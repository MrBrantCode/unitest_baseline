"""
QUESTION:
Write a function `validate_json_structure(json_string)` that validates the structure of a given JSON string. The function should verify that the brackets are properly opened and closed, key-value pairs are correctly formatted, data types are JSON supported, and JSON objects and arrays are properly structured and ended. String values must be enclosed in double-quotes. The function should return `True` if the JSON string is valid and `False` otherwise.
"""

import json

def validate_json_structure(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False