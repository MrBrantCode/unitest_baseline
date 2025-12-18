"""
QUESTION:
Write a function named `flatten_array` that takes a two-dimensional array of integers as input and returns a one-dimensional array containing all non-negative integers from the input array.
"""

def flatten_array(arr):
    """Flatten a two-dimensional array and exclude negative numbers."""
    flattened = []
    for sublist in arr:
        for num in sublist:
            if num >= 0:
                flattened.append(num)
    return flattened