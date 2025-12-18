"""
QUESTION:
Write a function named `count_string_values` that takes a JSON structure as input and returns the total count of all the string values in the structure. The JSON structure can have nested objects and arrays, and the values can be of any type (string, number, boolean, null). The count should only include the string values, and not count any other types of values, even if they appear multiple times in the structure.
"""

import json

def count_string_values(json_structure):
    count = 0
    if isinstance(json_structure, dict):
        for value in json_structure.values():
            if isinstance(value, str):
                count += 1
            elif isinstance(value, (dict, list)):
                count += count_string_values(value)
    elif isinstance(json_structure, list):
        for item in json_structure:
            count += count_string_values(item)
    return count