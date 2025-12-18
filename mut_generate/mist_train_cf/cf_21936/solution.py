"""
QUESTION:
Write a function `remove_value` that takes a nested dictionary `nested_dict` and a value `value` as input. The function should remove all occurrences of `value` from `nested_dict` and also remove any empty dictionaries or lists that are left behind. The function should be able to handle the removal of `value` for different data types such as strings, integers, and booleans. The time complexity of the function should be O(n), where n is the total number of elements in the nested dictionary.
"""

def remove_value(nested_dict, value):
    if isinstance(nested_dict, dict):
        for key, val in list(nested_dict.items()):
            if val == value:
                nested_dict.pop(key)
            elif isinstance(val, (dict, list)):
                remove_value(val, value)
            if isinstance(val, dict) and not val:
                nested_dict.pop(key)
    elif isinstance(nested_dict, list):
        for item in list(nested_dict):
            if item == value:
                nested_dict.remove(item)
            elif isinstance(item, (dict, list)):
                remove_value(item, value)
            if isinstance(item, dict) and not item:
                nested_dict.remove(item)
    return nested_dict