"""
QUESTION:
Write a function named `swap_elements` that takes an array and two indices `i` and `j` as input, and swaps the elements at indices `i` and `j` in the array directly without using a temporary variable. The function should handle cases where the indices `i` and `j` are out of bounds, the same, or the array is empty, contains duplicate values, negative values, or has only one element.
"""

def swap_elements(arr, i, j):
    # Check if the indices are out of bounds
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr):
        return arr
    
    # Check if the indices are the same
    if i == j:
        return arr
    
    # Perform the swap without using a temporary variable
    arr[i], arr[j] = arr[j], arr[i]
    
    return arr