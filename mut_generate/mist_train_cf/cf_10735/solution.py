"""
QUESTION:
Write a function `search(arr, target)` that searches for the target number in a given sorted array and returns the index of its leftmost occurrence if found, or -1 if not found. The function should have a time complexity of O(log n), where n is the length of the array, and should be able to handle large input arrays with up to 10^6 elements. The function should use an iterative approach with a modified binary search algorithm.
"""

def entance(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1