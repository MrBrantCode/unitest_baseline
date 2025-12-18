"""
QUESTION:
Create a function `merge_dicts(dict1, dict2)` that merges two dictionaries, maintaining their unique entries, and handles cases where duplicate keys have different values by taking the value from the first dictionary. The function should not use pre-built methods such as `dict.update()`.
"""

def merge_dicts(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        result[key] = value
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
    return result