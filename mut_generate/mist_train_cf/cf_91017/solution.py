"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array in ascending order and a target element as input. The function should return the index of the first occurrence of the target element in the array. If the target element is not found, return -1. The array may contain duplicate elements.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # look for first occurrence in the left half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result