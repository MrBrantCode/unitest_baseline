"""
QUESTION:
Create a function `binary_search` that performs recursive binary search in a sorted array of distinct elements. The function should return the index of the target element if found, or -1 if the target is not present. The implementation should have a time complexity of O(log n) and should not use any built-in search functions, libraries, or auxiliary data structures.
"""

def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)