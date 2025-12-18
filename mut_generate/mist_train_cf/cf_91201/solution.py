"""
QUESTION:
Implement the `binary_search` function, which takes a sorted list of integers `arr` in ascending order and a target integer `target` as input, and returns the index of the target in the list if found, or -1 if not found. The function should have a time complexity of O(log n) and should not use any built-in search functions or libraries.
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1