"""
QUESTION:
Write a function `count_string_values(json_str)` that takes a JSON string as input, parses it into a JSON object, and returns the total count of all string values in the object. The function should handle nested objects and arrays, and only count string values, excluding other types. If the input JSON string is invalid, the function should return an error message.
"""

import json

def count_string_values(json_str):
    def count_strings(obj):
        if isinstance(obj, str):
            return 1
        elif isinstance(obj, list):
            count = 0
            for item in obj:
                count += count_strings(item)
            return count
        elif isinstance(obj, dict):
            count = 0
            for value in obj.values():
                count += count_strings(value)
            return count
        else:
            return 0

    try:
        json_obj = json.loads(json_str)
        return count_strings(json_obj)
    except json.JSONDecodeError:
        return "Invalid JSON"