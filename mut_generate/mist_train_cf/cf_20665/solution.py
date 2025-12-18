"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list `arr` and a target element `target` as input. The function should return the index of the first occurrence of the target element in the list if found, or -1 if not found. The function should have a time complexity of O(log n) and be able to handle duplicate elements in the list.
"""

def binary_search(arr, target):
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