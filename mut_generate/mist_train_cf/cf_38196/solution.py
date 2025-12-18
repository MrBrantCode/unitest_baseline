"""
QUESTION:
Write a function `validate_profile` that takes a dictionary `profile` as input. The dictionary values are objects with attributes `opt` and `max`, each being a tuple of four integers. Return `True` if all the following conditions are met for each dictionary value: 
1. The `opt` tuple contains non-negative integers.
2. The `max` tuple contains non-negative integers.
3. Each element in the `opt` tuple is less than or equal to the corresponding element in the `max` tuple.
Otherwise, return `False`.
"""

def validate_profile(profile):
    for value in profile.values():
        if not (all(x >= 0 for x in value.opt) and all(x >= 0 for x in value.max)):
            return False
        if not all(opt <= max for opt, max in zip(value.opt, value.max)):
            return False
    return True