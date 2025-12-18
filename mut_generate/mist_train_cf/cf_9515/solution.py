"""
QUESTION:
Write a function `find_max_value(dictionary)` that finds the maximum value in a nested dictionary. The function should be able to handle dictionaries of any depth, with any number of keys and values at each level. The dictionary only contains numbers and other dictionaries as values.
"""

def find_max_value(dictionary):
    max_value = float('-inf')
    for value in dictionary.values():
        if isinstance(value, dict):
            max_value = max(max_value, find_max_value(value))
        else:
            max_value = max(max_value, value)
    return max_value