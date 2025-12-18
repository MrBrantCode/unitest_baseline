"""
QUESTION:
Create a function `merge_dictionaries` that takes two dictionaries, `dict1` and `dict2`, as input parameters. The function should return a new dictionary containing only the keys that are present in both `dict1` and `dict2`, with each corresponding value being a tuple of the values from both `dict1` and `dict2` for those matching keys.
"""

def merge_dictionaries(dict1, dict2):
    new_dict = {}
    for key in dict1.keys():
        if key in dict2.keys():
            new_dict[key] = (dict1[key], dict2[key])
    return new_dict