"""
QUESTION:
Write a function `extract_key_value_pairs(json_string)` that takes a JSON string as input, extracts its key-value pairs, and returns them as a dictionary. The function should handle nested objects and arrays, as well as malformed JSON or invalid characters, by printing an error message and returning an empty dictionary in such cases.
"""

import json

def extract_key_value_pairs(json_string):
    """
    Extracts key-value pairs from a JSON string, handling nested objects and arrays.
    Returns a dictionary with the extracted key-value pairs.
    If the JSON string is invalid or contains unsupported characters, prints an error message and returns an empty dictionary.
    """
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