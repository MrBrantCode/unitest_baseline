"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of integers `arr` and a target integer `target` as parameters. The function should return the index of the target integer in the list if found; otherwise, it should return -1. The function must use the binary search algorithm and handle cases where the target integer is not in the list.
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1