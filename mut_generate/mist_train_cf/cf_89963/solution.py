"""
QUESTION:
Implement a recursive binary search function named `binary_search` that takes a sorted list of integers `arr`, a target element `target`, a lower index `low`, and an upper index `high` as parameters. The function should return both the element and its index if found. If the target element is duplicated, return the index of the first occurrence. The function should handle cases where the target element is not found, returning `None` and `-1` in such cases.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return None, -1

    mid = (low + high) // 2

    if arr[mid] == target:
        index = find_first_occurrence(arr, target, low, mid)
        return arr[index], index
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

def find_first_occurrence(arr, target, low, high):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid
        else:
            low = mid + 1
    return low