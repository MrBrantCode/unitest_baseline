"""
QUESTION:
Implement a function called `binary_search_last_occurrence` that finds the index of the last occurrence of a target element in a sorted array of integers. The function takes in three parameters: `arr` (a sorted array of integers), `target` (the element to search for), and `low` (the starting index of the search range, defaulting to 0). If the target element is not found, the function should return -1. Assume that the array `arr` is sorted in ascending order and does not contain any duplicates.
"""

def binary_search_last_occurrence(arr, target, low=0):
    if len(arr) == 0:
        return -1
    
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            if mid < len(arr) - 1 and arr[mid + 1] == target:
                low = mid + 1
            else:
                return mid
        
        elif arr[mid] > target:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return -1