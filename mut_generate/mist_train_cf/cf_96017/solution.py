"""
QUESTION:
Implement an iterative binary search function named `binary_search` that takes a sorted array `arr` and a target element `target` as input, and returns the index of the target element if found, or -1 if not found. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the size of the array.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1