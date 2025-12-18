"""
QUESTION:
Implement a function `binary_search_recursive` that recursively finds a target value in a sorted list. The function should take four parameters: a sorted list `arr`, a target value `target`, and the starting index `low` and ending index `high` of the range to search. The function should return the index of the target value in the list if found, and -1 otherwise. The implementation must have a time complexity of O(log n) and space complexity of O(log n).
"""

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target value is not present in the list

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)