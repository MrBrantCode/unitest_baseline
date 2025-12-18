"""
QUESTION:
Create a function called `binary_search` that takes in two arguments, a sorted array `arr` and a target number `target`. The function should use an iterative binary search algorithm to find the position of the `target` in the array and return its index. If the `target` is not found in the array, the function should return -1. The time complexity of the function should be O(log n), where n is the length of the array.
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

    return -1