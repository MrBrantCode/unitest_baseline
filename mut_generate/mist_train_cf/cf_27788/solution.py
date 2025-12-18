"""
QUESTION:
Create a function `remove_none_values` that takes a JSON object as input and returns a modified JSON object with all the `None` values removed. The function should handle nested objects and arrays within the JSON structure and return the resulting JSON object.
"""

import json

def remove_none_values(json_data):
    if isinstance(json_data, dict):
        return {key: remove_none_values(value) for key, value in json_data.items() if value is not None}
    elif isinstance(json_data, list):
        return [remove_none_values(item) for item in json_data if item is not None]
    else:
        return json_data