"""
QUESTION:
Write a function `sum_of_elements` that takes a dictionary as its parameter and returns the sum of all its integer elements, excluding any elements whose keys are numbers or whose values are not integers, but recursively summing elements of nested dictionaries.
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