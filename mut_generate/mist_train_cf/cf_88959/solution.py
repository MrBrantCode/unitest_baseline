"""
QUESTION:
Write a function `find_max_length(dictionary)` that finds the key with the maximum length value among its string values in a given dictionary. The function should handle nested dictionaries as values by recursively searching for the maximum length value among the string values within the nested dictionaries. The function should return a tuple containing the key with the maximum length value and its corresponding length.
"""

def entance(dictionary):
    max_key = ""
    max_length = 0

    for key, value in dictionary.items():
        if isinstance(value, dict):
            nested_max = entance(value)
            if nested_max[1] > max_length:
                max_key, max_length = nested_max
        elif isinstance(value, str):
            if len(value) > max_length:
                max_key, max_length = key, len(value)

    return max_key, max_length