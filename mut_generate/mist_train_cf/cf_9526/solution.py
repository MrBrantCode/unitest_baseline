"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array to find the index of a given target element. The function should take two parameters: `arr`, a sorted list of elements, and `target`, the element to be searched. The function should return the index of the target element if found, and -1 if not found. Assume the array is sorted in ascending order.
"""

def entrance(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1