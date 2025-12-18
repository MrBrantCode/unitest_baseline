"""
QUESTION:
Write a function `get_nested_keys_sum` that takes a nested dictionary `nested_dict` and a string `key` as parameters. The function should return the sum of all values associated with the given `key` in the `nested_dict`. If the `key` is not found, return 0. Assume the values associated with the given `key` are integers.
"""

def get_nested_keys_sum(nested_dict, key):
    sum_values = 0
    for k, v in nested_dict.items():
        if k == key:
            sum_values += v
        elif isinstance(v, dict):
            sum_values += get_nested_keys_sum(v, key)
    return sum_values