"""
QUESTION:
Write a function `remove_duplicates` that takes an array as input, removes duplicate values without using built-in methods or data structures to store unique values, and returns the updated array. The function should handle arrays containing non-integer values (including strings and objects) and nested arrays, removing duplicates from the entire nested structure.
"""

def remove_duplicates(arr):
    if not isinstance(arr, list):
        return arr

    unique_values = []

    for item in arr:
        if isinstance(item, list):
            item = remove_duplicates(item)
        if item not in unique_values:
            unique_values.append(item)

    return unique_values