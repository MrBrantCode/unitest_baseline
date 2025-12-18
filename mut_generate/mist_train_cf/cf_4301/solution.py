"""
QUESTION:
Write a function called `sum_of_elements` that takes a dictionary as a parameter and returns the sum of all its elements, excluding keys that are numbers and values that are dictionaries. If a value is a nested dictionary, recursively sum its elements.
"""

def sum_of_elements(dictionary):
    total = 0
    for key, value in dictionary.items():
        if isinstance(key, int) or isinstance(value, dict):
            continue
        if isinstance(value, int):
            total += value
        elif isinstance(value, dict):
            total += sum_of_elements(value)
    return total