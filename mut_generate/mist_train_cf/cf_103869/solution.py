"""
QUESTION:
Write a function named `swap_elements` that takes an array and two indices `i` and `j` as input, and swaps the elements at these indices in the array directly, without using a temporary variable. The function should handle the case where `i` equals `j` by not modifying the array.
"""

def swap_elements(arr, i, j):
    if i == j:
        return

    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]