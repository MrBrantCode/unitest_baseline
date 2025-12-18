"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted list `arr` to find the index of the first occurrence of the `target` element. The function should return the index of the element if found, or -1 if not found. The implementation should have a time complexity of O(log n) and be able to handle duplicate elements in the list.
"""

def entance(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Check if it's the first occurrence
            while mid > 0 and arr[mid-1] == target:
                mid -= 1
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1