"""
QUESTION:
Write a function called `extract_keys` that takes a JSON data as input and returns a list of all unique keys on every level in the JSON data. The function should handle edge cases, including empty nested data and repeated keys on different levels.
"""

import json

def extract_keys(json_data, keys_set=None):
    if keys_set is None:
        keys_set = set()
        
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            keys_set.add(key)
            extract_keys(value, keys_set)

    elif isinstance(json_data, list):
        for item in json_data:
            extract_keys(item, keys_set)
    
    return keys_set