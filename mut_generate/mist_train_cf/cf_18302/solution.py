"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input, removes duplicate elements while maintaining the original order, and returns the resulting array. The function should not use any additional data structures or built-in functions.
"""

def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements