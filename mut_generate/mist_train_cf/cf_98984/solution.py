"""
QUESTION:
Implement a function `binary_search` that takes in a sorted array of integers `arr` and a target integer `target`, and returns the index of the target integer in the array. If the target integer is not found, return -1. The function should use the binary search algorithm and assume the input array is sorted in ascending order.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1