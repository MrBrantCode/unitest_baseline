"""
QUESTION:
Write a function `binary_search` that takes a sorted array `arr` and an integer `n` as parameters. The function should return the index of the first occurrence of `n` in the array if `n` is present. If `n` is not present, the function should return -1. The function must have a time complexity of O(log n).
"""

def binary_search(arr, n):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    return -1