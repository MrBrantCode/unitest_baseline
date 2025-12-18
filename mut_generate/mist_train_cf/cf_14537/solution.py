"""
QUESTION:
Create a function named `binary_search_recursive` that performs recursive binary search in a sorted array. The function should take four parameters: a sorted array `arr`, a target element `target`, a start index `start`, and an end index `end`. It should return the index of the target element if found, or -1 if not present. The function should have a time complexity of O(log n) and should not use any built-in search functions or libraries.
"""

def binary_search_recursive(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, end)