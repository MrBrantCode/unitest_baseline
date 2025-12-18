"""
QUESTION:
Write a function called `merge_dictionaries` that merges two dictionaries, `dict1` and `dict2`, where the values are either dictionaries or numeric types (int or float). If the dictionaries have overlapping keys, the function should merge the sub-dictionaries if the corresponding values are both dictionaries, or add up the values if they are both numbers. If a key from `dict2` is not found in `dict1`, the key-value pair should be added to `dict1`. The function should return the modified `dict1` as the result.
"""

def merge_dictionaries(dict1, dict2):
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merge_dictionaries(dict1[key], dict2[key])
            elif isinstance(dict1[key], (int, float)) and isinstance(dict2[key], (int, float)):
                dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1