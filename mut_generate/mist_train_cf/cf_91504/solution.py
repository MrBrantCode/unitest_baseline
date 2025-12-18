"""
QUESTION:
Create a function named `search` that takes a sorted array `arr` and a target number `target` as input, and returns the index of the first occurrence of `target` if it exists in `arr`, or -1 if it does not. The function should have a time complexity of O(log n), where n is the length of `arr`, and should be able to handle large input arrays efficiently with a maximum length of 10^6. If `arr` contains duplicate elements, the function should return the index of the leftmost occurrence of `target`. The function should use an iterative approach.
"""

def search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            # Check if the current element is the leftmost occurrence
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1