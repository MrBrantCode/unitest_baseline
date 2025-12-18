"""
QUESTION:
Create a function `flatten_dictionary` that takes a dictionary as input and returns a flattened dictionary. The function should be able to handle nested dictionaries of arbitrary depth, and the keys of the output dictionary should be in the format "parentkey_childkey" for nested keys. The function should also remove any duplicate values from the flattened dictionary. The function should use recursion and have a time complexity of O(n), where n is the total number of elements in the input dictionary.
"""

def entance(input_dict):
    flattened_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            flattened_value = entance(value)
            for sub_key, sub_value in flattened_value.items():
                if key:
                    if sub_key:
                        new_key = key + "_" + sub_key
                    else:
                        new_key = key
                else:
                    new_key = sub_key
                flattened_dict[new_key] = sub_value
        else:
            flattened_dict[key] = value
    # Remove duplicate values
    unique_values = list(set(flattened_dict.values()))
    unique_dict = {}
    for key, value in flattened_dict.items():
        if value in unique_values:
            unique_dict[key] = value
            unique_values.remove(value)
    return unique_dict