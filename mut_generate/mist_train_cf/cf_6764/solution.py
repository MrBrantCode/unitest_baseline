"""
QUESTION:
Write a function `linear_search_last(arr, target)` that returns the index of the last occurrence of the target element in the given array `arr`. The target element can be a string or an integer, and the array can have duplicate elements. If the target element is not present in the array, return -1.
"""

def linear_search_last(arr, target):
    last_index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            last_index = i
    return last_index