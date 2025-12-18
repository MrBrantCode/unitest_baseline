"""
QUESTION:
Write a function named `binary_search` that takes a sorted array `arr` and a target value `target` as input, and returns the index of the target if found, or -1 if not found. The function should have a time complexity of O(log n), where n is the length of the array, and should not use any built-in search functions or libraries. The array may contain duplicate elements.
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