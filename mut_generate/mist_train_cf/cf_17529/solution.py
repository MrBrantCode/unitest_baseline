"""
QUESTION:
Implement a function `binary_search_recursive` that takes a sorted list `data`, a target number `target`, and two indices `low` and `high` as input. The function should use the binary search algorithm recursively to find the index of the first occurrence of the `target` in the `data` list. If the `target` is not found, return -1. The time complexity of the function should be O(log n), where n is the size of the `data` list.
"""

def binary_search_recursive(data, target, low, high):
    # Base case: target number not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # If the target number is found, check if it's the first occurrence
    if data[mid] == target:
        if mid == 0 or data[mid-1] != target:
            return mid
        else:
            return binary_search_recursive(data, target, low, mid-1)
    
    # If the target number is smaller, search in the left half
    elif data[mid] > target:
        return binary_search_recursive(data, target, low, mid-1)
    
    # If the target number is larger, search in the right half
    else:
        return binary_search_recursive(data, target, mid+1, high)