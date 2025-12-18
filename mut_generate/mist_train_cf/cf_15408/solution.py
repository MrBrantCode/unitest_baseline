"""
QUESTION:
Implement the function `binary_search_smallest(arr, target)` that performs a binary search on the given sorted array `arr` to find the index of the smallest element that is greater than or equal to the given `target` value. If no such element exists, return -1. Assume the input array is sorted in ascending order.
"""

def binary_search_smallest(arr, target):
    left = 0
    right = len(arr) - 1
    smallest = float('inf')
    
    while left <= right:
        middle = (left + right) // 2
        
        if arr[middle] >= target:
            smallest = min(smallest, arr[middle])
            right = middle - 1
        else:
            left = middle + 1
    
    if smallest == float('inf'):
        return -1
    else:
        return arr.index(smallest)