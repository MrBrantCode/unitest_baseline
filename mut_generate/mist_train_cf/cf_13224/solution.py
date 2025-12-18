"""
QUESTION:
Write a Python function `sum_of_integers` that takes a dictionary as input and returns the sum of all integer values in the dictionary, including those in nested dictionaries. The function should be able to handle dictionaries with multiple levels of nesting.
"""

def sum_of_integers(dictionary):
    total_sum = 0
    for key, value in dictionary.items():
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, dict):
            total_sum += sum_of_integers(value)
    return total_sum