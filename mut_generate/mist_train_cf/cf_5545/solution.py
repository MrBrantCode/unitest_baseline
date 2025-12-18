"""
QUESTION:
Design a function `search_element(arr, x)` to search for a given element `x` in a sorted vector `arr` with a time complexity of O(log n), where n is the number of elements in the vector. The vector is sorted in ascending order and may contain duplicate elements. If the target element `x` is found, the function should return the index of its first occurrence. If `x` is not found, the function should return -1.
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