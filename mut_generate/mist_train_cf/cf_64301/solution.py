"""
QUESTION:
Create a function named `dict_to_list` that transforms the key-value pairs of a dictionary into a new list of strings, where each string is in the format "key: value". The function should take a dictionary as input and return the resulting list. The function should be optimized for readability and efficiency.
"""

def dict_to_list(input_dict):
    return [f"{key}: {value}" for key, value in input_dict.items()]