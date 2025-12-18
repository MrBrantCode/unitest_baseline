"""
QUESTION:
Write a function called `sum_dictionary` that takes a dictionary with integer and/or nested dictionary values as input and returns the sum of all integers in the dictionary. The function should recursively calculate the sum of integers in nested dictionaries and skip non-integer values.
"""

def sum_dictionary(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, int):
            total += value
        elif isinstance(value, dict):
            total += sum_dictionary(value)
    return total