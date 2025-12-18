"""
QUESTION:
Implement a function `binary_search` that performs a recursive binary search on a sorted array to find the index of a given target value. The function should take in the array, the target value, and the low and high indices of the search space as parameters. The function should return the index of the target value if found, and -1 otherwise. The function should have a time complexity of O(log n).
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)