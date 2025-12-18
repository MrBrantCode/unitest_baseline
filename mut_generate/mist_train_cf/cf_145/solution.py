"""
QUESTION:
Implement a function named `sum_array` that takes an array of integers as input and returns their sum. The solution must not use the built-in sum() function or any loop structures. The function should be implemented recursively and work for non-empty arrays.
"""

def sum_array(arr):
    return arr[0] if len(arr) == 1 else arr[0] + sum_array(arr[1:])