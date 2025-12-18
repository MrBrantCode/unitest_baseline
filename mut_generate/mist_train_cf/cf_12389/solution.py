"""
QUESTION:
Write a function `binary_search(arr, target)` that takes a sorted array `arr` and a number `target` as input, and returns the index of `target` in the array if it exists, or -1 if it does not exist. The function must have a time complexity of O(log n), where n is the length of the array, and must use an iterative binary search algorithm.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # target not found in the array