"""
QUESTION:
Write a function named `reverse_second_level` that takes a nested dictionary as input and reverses the order of keys at the second level while preserving the original order of keys at the first level. The function should return a tuple containing the modified dictionary and a list of values whose keys were initially last within each inner dictionary.
"""

def reverse_second_level(nested_dict):
    result = {}
    last_values = []
    for key in nested_dict:
        inner_dict = nested_dict[key]
        reversed_inner_dict = {k: v for k, v in reversed(list(inner_dict.items()))}
        result[key] = reversed_inner_dict
        last_values.append(list(reversed_inner_dict.values())[0])
    return result, last_values