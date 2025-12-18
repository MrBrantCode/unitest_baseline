"""
QUESTION:
Create a function `dig_and_sum` that takes a dictionary as input and returns the sum of all integers in the dictionary. The dictionary can have nested dictionaries as values, and the function should recursively traverse these nested dictionaries to find all integers. The function should only sum up integer values and ignore other types of values.
"""

def dig_and_sum(dictionary):
    total = 0
    for key, value in dictionary.items():
        if isinstance(value, dict):
            total += dig_and_sum(value)
        elif isinstance(value, int):
            total += value
    return total