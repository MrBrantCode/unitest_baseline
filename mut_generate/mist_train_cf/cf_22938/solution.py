"""
QUESTION:
Write a function `multiply_dicts` that takes two dictionaries `d1` and `d2` as input and returns a new dictionary with the values from `d1` multiplied by the corresponding values from `d2` if the key exists in `d2`, otherwise the original value from `d1`.
"""

def multiply_dicts(d1, d2):
    result = {}
    for key in d1:
        if key in d2:
            result[key] = d1[key] * d2[key]
        else:
            result[key] = d1[key]
    return result