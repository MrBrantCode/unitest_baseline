"""
QUESTION:
Implement the `binary_search` function to find the index of a target element in a sorted array. The function should take four parameters: a sorted array `arr`, a target element `target`, and two indices `start` and `end` representing the range of the array to search in. The function should return the index of the target element if found, and -1 otherwise. The array indices are 0-based.
"""

def binary_search(arr, target, start, end):
    if start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        else:
            return binary_search(arr, target, mid + 1, end)

    else:
        return -1