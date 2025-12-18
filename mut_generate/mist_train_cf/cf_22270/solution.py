"""
QUESTION:
Design a function named `binary_search` that takes a sorted array `arr` and a target element `target` as input, and returns the index of the target element if it exists in the array, or -1 otherwise. The function should have a time complexity of O(log n), where n is the number of elements in the array, and should not use any built-in search functions or libraries.
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