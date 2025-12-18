"""
QUESTION:
Implement a binary search function named `binary_search` that takes a sorted array of integers `arr` and a target integer `target` as input, and returns the index of the target in the array if found, or -1 otherwise. The function should limit the number of iterations to the least possible and provide a clear and concise implementation of the algorithm. The array is 0-indexed.
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