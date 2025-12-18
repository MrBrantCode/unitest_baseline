"""
QUESTION:
Write a function named `extract_key_value_pairs` that takes a JSON string as input and returns a dictionary containing all key-value pairs in the JSON data. The function should handle nested objects and arrays, and it should return an empty dictionary if the input JSON string is malformed or contains invalid characters.
"""

import json

def extract_key_value_pairs(json_string):
    try:
        json_data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
        return {}

    pairs = {}

    def extract(obj, path=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                extract(value, new_path)
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                new_path = f"{path}[{index}]"
                extract(value, new_path)
        else:
            pairs[path] = obj

    extract(json_data)
    return pairs