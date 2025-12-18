"""
QUESTION:
Create a function named `multiply_dicts` that takes two dictionaries, `dict1` and `dict2`, as parameters. The function should return a new dictionary where the values are the product of corresponding values in `dict1` and `dict2` if the key exists in both dictionaries. If a key only exists in `dict1`, its value in the new dictionary should be the same as in `dict1`. Keys that only exist in `dict2` should be ignored. The function should return a dictionary with all keys from `dict1` and the updated values.
"""

def multiply_dicts(dict1, dict2):
    return {k: dict1[k] * dict2[k] if k in dict2 else dict1[k] for k in dict1}