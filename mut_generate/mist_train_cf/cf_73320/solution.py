"""
QUESTION:
Create a function named `exclude_from_dict` that takes two parameters: a dictionary `my_dict` and a list `exclude`. The function should return a new dictionary that contains all key-value pairs from `my_dict` except for the keys specified in the `exclude` list.
"""

def exclude_from_dict(my_dict, exclude):
    return {key: my_dict[key] for key in my_dict if key not in exclude}