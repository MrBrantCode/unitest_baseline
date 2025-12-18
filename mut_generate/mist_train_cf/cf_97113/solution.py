"""
QUESTION:
Implement a function `count_string_values` that takes a JSON structure as input and returns the total count of all the string values in the structure. The function should recursively traverse the JSON structure, which can contain nested objects and arrays with values of any type (string, number, boolean, null), and only count the string values.
"""

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