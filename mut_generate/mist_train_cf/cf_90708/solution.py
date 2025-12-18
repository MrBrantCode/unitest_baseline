"""
QUESTION:
Create a function named `binary_search` that takes a sorted list of integers and a target integer as input, and returns the index of the target integer if it exists in the list. If the target integer does not exist, the function should return -1. The function must have a time complexity of O(log n), where n is the length of the list. The input list is guaranteed to be sorted.
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