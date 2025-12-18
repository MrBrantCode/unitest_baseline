"""
QUESTION:
Write a function `sum_positive_elements` that takes a dictionary as input where keys are strings and values are either positive integers or dictionaries following the same format. The function should recursively sum up all positive integers across all levels of nesting in the dictionary with a time complexity of O(n), where n is the total number of positive integers.
"""

def sum_positive_elements(dictionary):
    total = 0
    for value in dictionary.values():
        if isinstance(value, dict):
            total += sum_positive_elements(value)
        elif isinstance(value, int) and value > 0:
            total += value
    return total