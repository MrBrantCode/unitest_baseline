"""
QUESTION:
Implement a function named `find_max_min` that takes an array of integers as input and returns the maximum and minimum values of the array. The function should have a time complexity of O(n), where n is the length of the array, and cannot use any built-in sorting functions or data structures.
"""

def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    return max_val, min_val