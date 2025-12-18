"""
QUESTION:
Write a function `swap_elements(arr, i, j)` that swaps the elements at indices `i` and `j` in the array `arr` directly, without using a temporary variable. The function should handle cases where `i` and `j` are out of bounds, equal, or refer to elements in an array that is empty, contains duplicate values, contains negative values, or has only one element.
"""

def swap_elements(arr, i, j):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr):
        return arr
    if i == j:
        return arr
    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]
    return arr