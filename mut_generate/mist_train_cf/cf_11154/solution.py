"""
QUESTION:
Write a function `format_json(json_string)` that formats a valid JSON string with arbitrary key-value pairs and nested objects or arrays into a string with indentation of 4 spaces. The function should return the formatted JSON string if the input is valid and an error message if the input is an invalid JSON string.
"""

import json

def format_json(json_string):
    try:
        json_object = json.loads(json_string)
        formatted_json = json.dumps(json_object, indent=4)
        return formatted_json
    except json.JSONDecodeError:
        return "Invalid JSON string"