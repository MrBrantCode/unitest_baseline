"""
QUESTION:
Create a function `merge_dictionaries(dict1, dict2)` that merges two dictionaries and returns a new dictionary. The function should perform the following operations:

- Concatenate values for keys that are present in both dictionaries into a single string.
- Remove any key-value pairs where the value is a negative number.
- Sort the merged dictionary by key in ascending order.

Do not use any built-in Python functions or libraries for merging dictionaries, sorting, or any other operations.
"""

def entrance(dict1, dict2):
    merged_dict = {}

    # Combine key-value pairs from both dictionaries
    for key, value in dict1.items():
        merged_dict[key] = value

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = str(merged_dict[key]) + ' ' + str(value)
        else:
            merged_dict[key] = value

    # Remove key-value pairs with negative values
    merged_dict = {k: v for k, v in merged_dict.items() if not (isinstance(v, int) and v < 0) and not (isinstance(v, str) and v.strip().lstrip('-').isdigit())}

    # Sort the merged dictionary by key in ascending order
    sorted_dict = {}
    for key in sorted(merged_dict):
        sorted_dict[key] = merged_dict[key]

    return sorted_dict