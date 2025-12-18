"""
QUESTION:
Design a function named `select_nth_smallest` that takes two parameters: an array `arr` and an integer `n`. The function should return the nth smallest element from the array. If `n` is greater than the length of the array, the function should return -1. The array can be of any length, may contain duplicate elements, and may be sorted in ascending or descending order. The function should handle edge cases where the array is empty.
"""

def select_nth_smallest(arr, n):
    # Check if n is greater than the length of the array
    if n > len(arr):
        return -1

    # Handle the case where the array is empty
    if len(arr) == 0:
        return -1

    # Sort the array in ascending order
    arr.sort()

    # Return the nth smallest element
    return arr[n-1]