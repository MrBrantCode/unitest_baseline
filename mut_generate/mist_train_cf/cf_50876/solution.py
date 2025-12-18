"""
QUESTION:
Write a function `merge_dict(dict1, dict2)` that merges two dictionaries into one. The function should return an error message if either dictionary is not a dictionary, or if any key in either dictionary is not an integer, or if any value in either dictionary is not a string. If both dictionaries share a key, the function should concatenate the corresponding values in the resulting dictionary.
"""

def merge_dict(dict1, dict2):
    # Error checking: all keys and values are of correct types
    try:
        for k, v in dict1.items():
            if not isinstance(k, int) or not isinstance(v, str):
                return "Error: All keys should be integers and all values should be strings."
        for k, v in dict2.items():
            if not isinstance(k, int) or not isinstance(v, str):
                return "Error: All keys should be integers and all values should be strings."
    except AttributeError:
        return "Error: Inputs should be dictionaries."

    # Merging the dictionaries
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict