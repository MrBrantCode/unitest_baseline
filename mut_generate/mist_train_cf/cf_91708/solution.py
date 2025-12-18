"""
QUESTION:
Write a function `format_json(json_string)` that formats a given JSON string into a pretty-printed JSON string with 4-space indentation. The function should be able to handle any valid JSON string, including those with arbitrary key-value pairs and nested objects or arrays. If the input string is not a valid JSON, the function should return an error message.
"""

import json

def format_json(json_string):
    try:
        json_object = json.loads(json_string)
        formatted_json = json.dumps(json_object, indent=4)
        return formatted_json
    except json.JSONDecodeError:
        return "Invalid JSON string"