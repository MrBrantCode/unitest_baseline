"""
QUESTION:
Implement a function named `binary_search` that checks whether a given target element is present in a sorted array in ascending order. The function should have a time complexity of O(log n), where n is the size of the array, and must handle duplicate elements correctly, returning true if at least one occurrence of the target element is present. The function should take two parameters: a sorted array `arr` and a target element `target`, and return a boolean value indicating whether the target element is present in the array.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False