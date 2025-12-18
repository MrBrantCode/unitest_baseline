"""
QUESTION:
Create a function called `create_nested_dict` that takes two lists, `keys` and `values`, as input and returns a nested dictionary where each key in the outer dictionary corresponds to a dictionary with the same keys as the input `keys` list and values calculated by multiplying the corresponding value from the `values` list with each key.
"""

def create_nested_dict(keys, values):
    return {key: {inner_key: inner_key*value for inner_key in keys} for key, value in zip(keys, values)}