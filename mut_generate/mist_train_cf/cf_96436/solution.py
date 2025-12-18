"""
QUESTION:
Implement a function called `binary_search` that recursively finds the index of the first occurrence of a target value in a sorted array. The function should take four parameters: a sorted array `arr`, a target value `target`, and two indices `low` and `high` representing the current search range. If the target value is not found in the array, the function should return -1.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        # Check if this is the first occurrence of the target
        if mid == 0 or arr[mid - 1] != target:
            return mid
        else:
            # Recursively search on the left side for the first occurrence
            return binary_search(arr, target, low, mid - 1)
    elif arr[mid] > target:
        # Recursively search on the left side
        return binary_search(arr, target, low, mid - 1)
    else:
        # Recursively search on the right side
        return binary_search(arr, target, mid + 1, high)