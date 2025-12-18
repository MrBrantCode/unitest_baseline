"""
QUESTION:
Implement a function `search` that finds the index of the first occurrence of a target element in a sorted array with duplicates, returning -1 if not found. The function should have a time complexity of O(log n), where n is the size of the array.
"""

def search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Continue searching in the left half to find the first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result