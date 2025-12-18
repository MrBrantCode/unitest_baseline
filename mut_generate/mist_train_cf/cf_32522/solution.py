"""
QUESTION:
Write a function `custom_json_sort` that takes a dictionary `json_obj` as input and returns a string representation of the dictionary with its keys sorted in ascending order and indentation. The function should also handle nested dictionaries by sorting their keys in ascending order.
"""

import json

def custom_json_sort(json_obj: dict) -> str:
    sorted_json = json.dumps(json_obj, indent=4, sort_keys=True)
    return sorted_json