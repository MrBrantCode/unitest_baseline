"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted list `arr` to find if the `target` exists. The function should have a time complexity of O(log n) and handle the case where the list contains only one item.
"""

def binary_search(arr, target):
    if len(arr) == 1:
        return arr[0] == target
    
    if len(arr) == 0:
        return False
    
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr[mid+1:], target)
    else:
        return binary_search(arr[:mid], target)