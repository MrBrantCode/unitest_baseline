"""
QUESTION:
Implement a function called `binary_search` that takes in a sorted array `arr`, a target element `target`, and two indices `low` and `high` representing the current search range within the array. The function should return the position of the first occurrence of the target element in the array if found, or -1 if not found. The function must be implemented recursively and assumes the input array is sorted in ascending order.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        if mid == 0 or arr[mid - 1] != target:
            return mid
        else:
            return binary_search(arr, target, low, mid - 1)
    
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    
    else:
        return binary_search(arr, target, low, mid - 1)