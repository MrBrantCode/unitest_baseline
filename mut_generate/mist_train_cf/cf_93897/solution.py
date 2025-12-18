"""
QUESTION:
Implement a function named `binary_search_recursive` that performs a recursive binary search on a sorted list to find a specific target value. The function should take four parameters: a sorted list `arr`, the target value `target`, the lowest index `low`, and the highest index `high`. The function should return the index of the target value if found, and -1 otherwise. The list is sorted in ascending order, and the function should use recursion to achieve the binary search.
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