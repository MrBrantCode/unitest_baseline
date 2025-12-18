"""
QUESTION:
Implement a function named `binary_search_recursive` that takes a sorted list `arr`, a target value `target`, and the lowest index `low` and highest index `high` as parameters. The function should use a recursive binary search algorithm to find the target value in the list. If the target value is found, return its index; otherwise, return -1. The input list is sorted in ascending order.
"""

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)