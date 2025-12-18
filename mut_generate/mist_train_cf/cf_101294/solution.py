"""
QUESTION:
Implement the `binary_search` function, which takes a sorted array of integers `arr` and a target integer `target` as input. The function should return the index of the target integer in the array using the binary search algorithm. If the target integer is not found, return -1. The input array is guaranteed to be sorted in ascending order.
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