"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array of integers `arr` and a target integer `target` as input and returns the index of `target` in `arr` if found, or -1 otherwise. The function should use the binary search algorithm to minimize the number of iterations.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1