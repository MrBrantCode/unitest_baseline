"""
QUESTION:
Implement a function `modifiedLinearSearch(arr, target)` that performs a modified linear search in a sorted array `arr` to find the index of the first occurrence of `target`. The function should return the index of `target` if found, and -1 otherwise. The function should handle duplicate elements by continuing to search until the last occurrence of a duplicate element. Assume that the input array is sorted in non-decreasing order.
"""

def modifiedLinearSearch(arr, target):
    n = len(arr)
    i = 0
    
    while i < n and arr[i] <= target:
        if arr[i] == target:
            return i
        i = i + 1
    
    return -1