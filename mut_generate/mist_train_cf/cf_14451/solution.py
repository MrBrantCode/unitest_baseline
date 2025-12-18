"""
QUESTION:
Write a function `is_valid_json_with_nested_structure(json_string)` that takes a string `json_string` as input and returns a boolean indicating whether the string is a valid JSON document that includes at least one nested object or array.
"""

import json
import re

def is_valid_json_with_nested_structure(json_string):
    pattern = r'^\s*(\{.*\}|\[.*\])\s*$'
    if not re.match(pattern, json_string):
        return False

    try:
        json_data = json.loads(json_string)
        if isinstance(json_data, dict):
            return any(isinstance(val, (dict, list)) for val in json_data.values())
        elif isinstance(json_data, list):
            return any(isinstance(item, (dict, list)) for item in json_data)
        else:
            return False
    except json.JSONDecodeError:
        return False