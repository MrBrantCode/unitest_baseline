"""
QUESTION:
Write a function `areInverse(arr1, arr2)` that checks if two arrays of integers are inverses of each other, accommodating for empty arrays and duplicate values. The function should return `True` if the arrays are inverses and `False` otherwise.
"""

def areInverse(arr1, arr2):
    return arr1 == arr2[::-1]  # Reverse arr2 by slicing