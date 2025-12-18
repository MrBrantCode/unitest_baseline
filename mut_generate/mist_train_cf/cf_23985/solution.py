"""
QUESTION:
Create a function named `count_unique_elements` that takes an array of integers as input and returns the number of unique elements present in the array. The array can contain duplicate elements, and the function should ignore these duplicates when calculating the count.
"""

def count_unique_elements(arr):
    """Returns the number of unique elements present in the given array."""
    unique_elements = set(arr)
    return len(unique_elements)