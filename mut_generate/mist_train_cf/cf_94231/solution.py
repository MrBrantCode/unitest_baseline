"""
QUESTION:
Implement the `binary_search` function, which takes a sorted array of integers and a target value as input, and returns the index of the target value in the array if found, or -1 if not found. The input array is guaranteed to be sorted in ascending order and may contain duplicate elements, be empty, or not contain the target value.
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