"""
QUESTION:
Given a list of integers 'b', apply an unknown set of recursive functions to 'b', sort the resulting list, and then perform a binary search on the sorted list. Write a function 'binary_search' that takes a sorted list 'arr', the low and high indices of the list, and a target value 'x' as input and returns the index of 'x' in 'arr' if found, otherwise -1. Assume the initial input list 'b' is [-2, -3, 7, 1, -8, 5, 11, -14, 20] and the target value 'x' is 7.
"""

def binary_search(arr, low, high, x):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1