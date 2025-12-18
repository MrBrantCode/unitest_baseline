"""
QUESTION:
Implement a function named `combine_dicts` that takes in three parameters: two dictionaries `d1` and `d2`, and a binary operation function `op`. The function should return a new dictionary where the elements of `d1` and `d2` are combined. If a key exists in both dictionaries, the function `op` should be applied to the corresponding values. If a key only exists in one dictionary, its value should be included in the resulting dictionary as is. The function `op` should be flexible enough to handle different operations such as summing numbers or concatenating strings.
"""

def combine_dicts(d1, d2, op):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] = op(result[key], value)
        else:
            result[key] = value
    return result