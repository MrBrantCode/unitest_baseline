"""
QUESTION:
Implement a function `sort_json(json_string)` that takes a JSON string as input, converts it into an array of key-value pairs, sorts the array in alphabetical order based on the keys, and removes duplicate keys by keeping only the last occurrence of each key. The function should handle nested objects and arrays in the JSON string.
"""

import json

def sort_json(json_string):
    def flatten_json(json_data, parent_key='', separator='.'):
        flattened_data = []
        for key, value in json_data.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            if isinstance(value, dict):
                flattened_data.extend(flatten_json(value, new_key, separator=separator))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    flattened_data.extend(flatten_json({str(i): item}, new_key, separator=separator))
            else:
                flattened_data.append((new_key, value))
        return flattened_data

    def remove_duplicates(sorted_data):
        unique_data = {}
        for key, value in sorted_data:
            unique_data[key] = value
        return list(unique_data.items())

    json_data = json.loads(json_string)
    flattened_data = flatten_json(json_data)
    sorted_data = sorted(flattened_data, key=lambda x: x[0])
    return remove_duplicates(sorted_data)