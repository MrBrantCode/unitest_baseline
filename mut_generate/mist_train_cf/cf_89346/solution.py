"""
QUESTION:
Write a Python function named `calculate_sum` that takes a dictionary as an argument and returns the sum of all integer values in the dictionary. The dictionary may contain nested dictionaries or lists, and the function should recursively calculate the sum of all integers, skipping non-integer values. The function should be able to handle multiple levels of nesting and different types of values, including lists and dictionaries.
"""

def calculate_sum(dictionary):
    total_sum = 0
    for value in dictionary.values():
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, dict):
            total_sum += calculate_sum(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, int):
                    total_sum += item
                elif isinstance(item, dict):
                    total_sum += calculate_sum(item)
    return total_sum