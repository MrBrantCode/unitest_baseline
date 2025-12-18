"""
QUESTION:
Write a function binary_search(arr, low, high, target) that uses a recursive binary search algorithm to find the index of a given number (target) in a sorted array of distinct integers in ascending order. The function should return the index of the target if found, and -1 otherwise, with a time complexity of O(log n).
"""

def entance(arr, low, high, target):
    # Base case: element not found
    if low > high:
        return -1
    
    # Find the middle index
    mid = (low + high) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    
    # Recursive cases: search in the left or right half of the array
    if arr[mid] > target:
        return entance(arr, low, mid - 1, target)
    else:
        return entance(arr, mid + 1, high, target)