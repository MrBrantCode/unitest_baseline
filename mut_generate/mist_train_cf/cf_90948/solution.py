"""
QUESTION:
Create a function `merge_dictionaries` that takes two dictionaries `dict1` and `dict2` as input and returns a new dictionary. The function should merge the key-value pairs from both input dictionaries, concatenate the values for keys that are present in both dictionaries, remove any key-value pairs where the value is a negative number, and sort the resulting dictionary by key in ascending order.
"""

def merge_dictionaries(dict1, dict2):
    merged_dict = {}

    # Combine key-value pairs from both dictionaries
    merged_dict.update(dict1)
    merged_dict.update(dict2)

    # Concatenate values for keys that are present in both dictionaries
    for key in dict1:
        if key in dict2:
            merged_dict[key] = str(dict1[key]) + ' ' + str(dict2[key])

    # Remove key-value pairs with negative values
    merged_dict = {k: v for k, v in merged_dict.items() if isinstance(v, str) or v >= 0}

    # Sort the merged dictionary by key in ascending order
    sorted_dict = {}
    for key in sorted(merged_dict):
        sorted_dict[key] = merged_dict[key]

    return sorted_dict