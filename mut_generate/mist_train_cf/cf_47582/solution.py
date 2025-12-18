"""
QUESTION:
Write a Python function called `dict_to_tuples` that takes a dictionary as input where the values can be either dictionaries or non-dictionary values. The function should return a list of tuples where each key-value pair from the input dictionary and its nested dictionaries is represented as a separate tuple. If a value is a dictionary, its key should be combined with its parent key using an underscore as a separator.
"""

def dict_to_tuples(input_dict):
    output_list = []
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                output_list.append((f"{key}_{sub_key}", sub_value))
        else:
            output_list.append((key, value))
    return output_list