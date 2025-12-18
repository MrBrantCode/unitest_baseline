"""
QUESTION:
Create a function `find_nested_keys` that retrieves the values of a specified key from a nested dictionary. The dictionary's structure and keys can vary, and the function should be able to handle multiple levels of nesting and multiple occurrences of the target key. The function should return a list of the found values in the order of discovery. If the target key is not found, return an empty list.
"""

def find_nested_keys(input_dict, target_key, result=None):
    if result is None:
        result = []
    for key, value in input_dict.items():
        if key == target_key:
            result.append(value)
        elif isinstance(value, dict):
            find_nested_keys(value, target_key, result)
    return result