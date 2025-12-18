"""
QUESTION:
Write a function `reverse_array` that takes an array `arr`, `start` index, and `end` index as parameters. The function should reverse the array in-place using a recursive approach without using any built-in array reversing functions or methods. The function should swap elements in the array such that the first element becomes the last, the second becomes the second last, and so on, until the middle of the array is reached. The original array should be modified.
"""

def reverse_array(arr, start, end):
    if start >= end:
        return
    
    # Swap the first and last elements
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursively reverse the rest of the array
    reverse_array(arr, start + 1, end - 1)