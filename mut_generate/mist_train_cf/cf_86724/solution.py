"""
QUESTION:
Write a function binary_search(arr, target) that takes a sorted array and a target value as input, and returns the index of the target if found, or -1 if not found. The array may contain duplicate elements, and the function should have a time complexity of O(log n), where n is the length of the array.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1