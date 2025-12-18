"""
QUESTION:
Implement a function `binary_search_recursive(arr, target, low, high)` that performs a recursive binary search on a sorted list `arr` to find a specific `target` value. The function should have a time complexity of O(log n) and space complexity of O(log n), where n is the size of the list. If the `target` value is found, return its index; otherwise, return -1.
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