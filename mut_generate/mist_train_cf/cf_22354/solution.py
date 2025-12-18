"""
QUESTION:
Write a function called `reverse_array` that takes an array and two indices, `start` and `end`, as parameters. The function should reverse the elements of the array in-place from the `start` index to the `end` index using a recursive approach, without utilizing any built-in array reversing functions or methods. The original array should be modified.
"""

def reverse_array(arr, start, end):
    if start >= end:
        return
    
    # Swap the first and last elements
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursively reverse the rest of the array
    reverse_array(arr, start + 1, end - 1)