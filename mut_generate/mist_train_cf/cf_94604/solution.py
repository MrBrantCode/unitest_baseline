"""
QUESTION:
Create a function `json_to_array` that takes a JSON string as input, parses it, and returns its contents as a sorted array of key-value pairs. The array elements should be sorted in alphabetical order based on the keys. The function should be able to handle JSON strings that contain nested objects and arrays.
"""

import json

def json_to_array(json_str):
    def sort_dict_items(dictionary):
        return sorted(dictionary.items(), key=lambda x: x[0])

    def process_nested(data):
        if isinstance(data, dict):
            sorted_items = sort_dict_items(data)
            return [[key, process_nested(value)] for key, value in sorted_items]
        elif isinstance(data, list):
            return [process_nested(item) for item in data]
        else:
            return data

    json_data = json.loads(json_str)
    sorted_data = process_nested(json_data)
    return sorted_data