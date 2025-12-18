"""
QUESTION:
Implement a recursive binary search function `binary_search(arr, low, high, x)` that finds the index of an element `x` in a sorted list `arr` without using loops or built-in sorting algorithms. The function should return the index of `x` if found, otherwise return -1. What is the time and space complexity of this function when executed with a list of size `n`, where `n` is a positive integer?
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