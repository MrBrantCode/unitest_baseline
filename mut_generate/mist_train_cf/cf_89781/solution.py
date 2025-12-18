"""
QUESTION:
Write a function `get_json_data_types` that takes a JSON string as input and returns a dictionary where the keys are the paths to each value (in dot notation) and the values are the corresponding data types. The function should support nested objects and the following data types: boolean, integer, string, null, and object. The time complexity of the solution should not exceed O(n), where n is the number of characters in the JSON string.
"""

import json

def get_data_type(value):
    if isinstance(value, bool):
        return 'boolean'
    elif isinstance(value, int):
        return 'integer'
    elif isinstance(value, str):
        return 'string'
    elif isinstance(value, list):
        return 'array'
    elif value is None:
        return 'null'
    else:
        return 'object'

def traverse_json(json_obj, path, result):
    for key, value in json_obj.items():
        new_path = f"{path}.{key}" if path else key

        if isinstance(value, dict):
            traverse_json(value, new_path, result)
        else:
            result[new_path] = get_data_type(value)

def get_json_data_types(json_str):
    json_obj = json.loads(json_str)
    result = {}
    traverse_json(json_obj, '', result)
    return result