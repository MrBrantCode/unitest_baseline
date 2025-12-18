"""
QUESTION:
Create a function `merge_dicts(dict1, dict2)` that merges two dictionaries `dict1` and `dict2` into a new dictionary. The function should perform the following operations:

- For keys present in both dictionaries, concatenate string values, add numeric values, or merge list values.
- Remove any key-value pairs with negative numeric values.
- Sort the merged dictionary by key in ascending order.

Implement the function without using any built-in Python functions or libraries for merging dictionaries, sorting, or other operations. The time complexity of the solution should be O(n), where n is the total number of key-value pairs in both dictionaries.
"""

def merge_dicts(dict1, dict2):
    merged_dict = {}

    # Concatenate values for keys present in both dictionaries
    for key in dict1.keys():
        if key in dict2.keys():
            if type(dict1[key]) == str and type(dict2[key]) == str:
                merged_dict[key] = dict1[key] + ' ' + dict2[key]
            elif type(dict1[key]) == int and type(dict2[key]) == int:
                merged_dict[key] = dict1[key] + dict2[key]
            elif type(dict1[key]) == list and type(dict2[key]) == list:
                merged_dict[key] = dict1[key] + dict2[key]
        else:
            merged_dict[key] = dict1[key]

    # Add key-value pairs from dict2 to merged_dict
    for key in dict2.keys():
        if key not in merged_dict.keys():
            merged_dict[key] = dict2[key]

    # Remove negative values from merged_dict
    for key in list(merged_dict.keys()):
        if type(merged_dict[key]) == int and merged_dict[key] < 0:
            del merged_dict[key]

    # Sort merged_dict by key in ascending order
    sorted_keys = sorted(merged_dict.keys())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = merged_dict[key]

    return sorted_dict