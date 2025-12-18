"""
QUESTION:
Implement a function named `find_max` that takes an array as input and returns the maximum number in the array. If the array is empty, the function should return `None`.
"""

def find_max(arr):
    if len(arr) == 0:
        return None
    else:
        return max(arr)