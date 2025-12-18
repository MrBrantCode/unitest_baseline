"""
QUESTION:
Write a function called `remove_duplicates` that takes an array as input, removes duplicate values from the array and any nested arrays within it, and returns the array with unique values. The function should not use any built-in methods or data structures to store unique values and should be able to handle arrays containing non-integer values.
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