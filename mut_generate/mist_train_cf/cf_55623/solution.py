"""
QUESTION:
Implement a function `binary_search` that uses binary search and recursion to find the index of a target element `x` in a given array `arr`. Ensure the array is sorted before performing the search. Additionally, implement a function `sort_array` to sort the array if needed. The function `binary_search` should take in four parameters: the array `arr`, the low index `low`, the high index `high`, and the target element `x`. It should return the index of `x` if found, and -1 otherwise. The function `sort_array` should take in the array `arr` and return the sorted array.
"""

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def sort_array(arr):
    arr.sort()
    return arr