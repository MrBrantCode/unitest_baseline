"""
QUESTION:
Create a function `count_elements(dictionary)` that takes a dictionary as input and returns the number of elements in the dictionary, excluding elements whose keys are numbers. The dictionary may contain nested dictionaries as values. The function should handle cases where the dictionary is empty or where the dictionary values are themselves dictionaries.
"""

def count_elements(dictionary):
    count = 0
    for key, value in dictionary.items():
        if not isinstance(key, int) and not isinstance(key, float):
            count += 1
        if isinstance(value, dict):
            count += count_elements(value)
    return count