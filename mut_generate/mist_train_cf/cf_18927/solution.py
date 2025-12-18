"""
QUESTION:
Write a function called `sum_positive_elements` that takes a dictionary as input and returns the sum of all positive integers in the dictionary. The dictionary can have string keys and integer or dictionary values, and can be nested up to any level. The function should only include positive integers in the sum, ignoring any negative integers or non-integer values.
"""

def sum_positive_elements(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, int) and value > 0:
            total += value
        elif isinstance(value, dict):
            total += sum_positive_elements(value)
    return total