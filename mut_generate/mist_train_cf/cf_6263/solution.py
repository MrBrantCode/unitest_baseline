"""
QUESTION:
Write a function called `calculate_sum` to calculate the sum of all integers in a dictionary. The dictionary may contain nested dictionaries, lists, or non-integer values. The function should recursively calculate the sum of all integers, including those in nested dictionaries and lists, and skip non-integer values.
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
    return total_sum