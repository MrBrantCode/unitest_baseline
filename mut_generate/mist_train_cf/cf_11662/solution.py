"""
QUESTION:
Write a function `find_largest_key` that finds the largest key in a dictionary and returns its corresponding value. The function should not use built-in functions for sorting or finding the maximum value. The dictionary may contain duplicate keys and the largest key may have multiple values.
"""

def find_largest_key(dictionary):
    largest_key = float('-inf')  # Initialize with negative infinity
    largest_value = None

    for key, value in dictionary.items():
        if key > largest_key:
            largest_key = key
            largest_value = value

    return largest_value