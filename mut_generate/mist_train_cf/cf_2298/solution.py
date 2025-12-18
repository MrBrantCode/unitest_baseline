"""
QUESTION:
Write a function called `binary_search` that takes a sorted array `arr` and a target element `target` as input, and returns the index of the target element in the array. If the target element is not found, return -1. The array may contain duplicates and is already sorted in ascending order. Optimize the function to have a time complexity of O(log n) and space complexity of O(1).
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1