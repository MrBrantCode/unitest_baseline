"""
QUESTION:
Write a function named `get_sum_of_integers` that takes a JSON object and a key as input and returns the sum of all integers associated with the given key. The key can be a nested key represented by dots, and the function should handle multiple nesting levels. If the key does not exist in the JSON data or does not point to a valid integer value, the function should return None.
"""

import json

def get_sum_of_integers(json_data, key):
    keys = key.split('.')  
    value = json_data

    try:
        for k in keys:
            value = value[k]  
    except KeyError:
        return None

    if isinstance(value, int):
        return value

    if isinstance(value, dict):
        return sum([v for k, v in value.items() if isinstance(v, int)])

    if isinstance(value, list):
        return sum([i for i in value if isinstance(i, int)])

    return None