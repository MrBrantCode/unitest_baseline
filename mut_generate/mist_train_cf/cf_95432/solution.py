"""
QUESTION:
Write a function `sum_positive_elements` that takes a dictionary as input and returns the sum of all positive integers in the dictionary, including those in nested dictionaries. The dictionary's keys are strings, and its values are either positive integers or dictionaries with the same structure.
"""

def sum_positive_elements(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, int) and value > 0:
            total += value
        elif isinstance(value, dict):
            total += sum_positive_elements(value)
    return total