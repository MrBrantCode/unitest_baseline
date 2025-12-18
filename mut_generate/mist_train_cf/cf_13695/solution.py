"""
QUESTION:
Write a function called binary_search that takes a sorted 1D array of integers and a target integer as input. Using a binary search algorithm, return the index of the target if it is present in the array. If the target is not found, return -1. The input array is guaranteed to be sorted in ascending order.
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

    return -1  # Target not found