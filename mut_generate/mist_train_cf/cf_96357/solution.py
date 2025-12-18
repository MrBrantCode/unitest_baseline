"""
QUESTION:
Implement a function called `binary_search` that takes in a sorted array `arr` and a target value `target`, and returns the index of the target value in the array if it exists, or -1 otherwise. Assume the array is sorted in ascending order and the target value is a single element.
"""

def binary_search(arr, target):
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