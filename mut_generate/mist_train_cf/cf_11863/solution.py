"""
QUESTION:
Implement a function `count_elements(dictionary)` that takes a dictionary as input and returns the number of elements in the dictionary, excluding any elements whose keys are numbers. The function should handle nested dictionaries and empty dictionaries.
"""

def count_elements(dictionary):
    count = 0
    for key, value in dictionary.items():
        if not isinstance(key, int) and not isinstance(key, float):
            count += 1
        if isinstance(value, dict):
            count += count_elements(value)
    return count