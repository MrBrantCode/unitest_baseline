"""
QUESTION:
Implement a function named `ternary_search` that performs a ternary search on a sorted array to find the index of a target value. The function should take two parameters: `arr` (the sorted array) and `to_find` (the target value). If the target value is found, return its index; otherwise, return -1. Assume the array is sorted in ascending order.
"""

def ternary_search(arr, to_find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == to_find:
            return mid1
        elif arr[mid2] == to_find:
            return mid2
        elif to_find < arr[mid1]:
            right = mid1 - 1
        elif to_find > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1