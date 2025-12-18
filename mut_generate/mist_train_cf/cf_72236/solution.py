"""
QUESTION:
Construct a function called `common_keys` that takes two dictionaries, `dict1` and `dict2`, as input and returns a list of keys that exist in both `dict1` and `dict2`. The order of the keys in the output list should match their order of appearance in `dict2`.
"""

def common_keys(dict1, dict2):
    return [key for key in dict2 if key in dict1]