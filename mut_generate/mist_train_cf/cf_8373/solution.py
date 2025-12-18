"""
QUESTION:
Implement the `last_occurrence` function to find the index of the last occurrence of a target number in a sorted array of positive integers. The function should take two parameters: `arr` (the sorted array) and `target` (the target number). If the target number does not exist in the array, return -1. The function should have a time complexity of O(log n), where n is the length of the array.
"""

def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result