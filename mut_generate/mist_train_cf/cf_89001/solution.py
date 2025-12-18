"""
QUESTION:
Write a function called `search_element` that takes a sorted array `arr` and an element `x` as input. The function should return the index of the first occurrence of `x` in `arr` using a time complexity of O(log n), where n is the number of elements in `arr`. If `x` is not found in `arr`, the function should return -1. The array `arr` is sorted in ascending order and may contain duplicate elements.
"""

def search_element(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == x:
            result = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
            
    return result