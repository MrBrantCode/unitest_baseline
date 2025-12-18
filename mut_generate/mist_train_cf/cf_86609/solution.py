"""
QUESTION:
Write a function called `custom_json_sort` and another function called `display_json_contents` to parse a JSON document, validate its structure, handle nested objects and arrays, and custom data types such as dates and complex numbers. The `custom_json_sort` function should implement a custom sorting algorithm to sort the JSON objects based on a specific key value in ascending order. Both functions should take into account the JSON document's nested structure. The `custom_json_sort` function should be able to handle lists and dictionaries.
"""

import json

def custom_json_sort(data, key):
    if isinstance(data, list):
        return sorted(data, key=lambda x: x.get(key, 0))
    elif isinstance(data, dict):
        return {k: custom_json_sort(v, key) for k, v in data.items()}
    else:
        return data

def display_json_contents(data):
    if isinstance(data, list):
        for item in data:
            display_json_contents(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(key + ": ")
                display_json_contents(value)
            else:
                print(key + ": " + str(value))
    else:
        print(data)