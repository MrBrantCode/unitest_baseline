"""
QUESTION:
Write a function `json_to_dict(json_str)` that takes a JSON string as input and converts it into a valid Python dictionary. The input JSON string can contain nested objects and arrays with multiple levels of nesting. If the JSON string contains duplicate keys, the function should overwrite the existing value with the new value. The function should also handle invalid JSON strings by catching any exceptions that occur during parsing.
"""

import json

def json_to_dict(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        print("Invalid JSON string.")
        return {}