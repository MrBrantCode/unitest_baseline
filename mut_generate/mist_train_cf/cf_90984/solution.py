"""
QUESTION:
Write a function called `find_max_element` that takes a dictionary with string keys and nested dictionaries as values as input. Each nested dictionary has string keys and numeric values. The function should return a tuple containing the key of the outer dictionary with the maximum sum of its nested dictionary's values, and the corresponding maximum sum. Assume that the input dictionary is not empty and all nested dictionaries are non-empty.
"""

def find_max_element(dictionary):
    max_value = float('-inf')
    max_key = None

    for key, nested_dict in dictionary.items():
        nested_sum = sum(nested_dict.values())
        if nested_sum > max_value:
            max_value = nested_sum
            max_key = key

    return max_key, max_value