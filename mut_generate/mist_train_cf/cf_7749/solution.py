"""
QUESTION:
Design a function `search(arr, target)` that searches for a target element in a sorted array `arr` with a time complexity of O(log n), where n is the number of elements in the array. The function should return `True` if the target element is found, and `False` otherwise. The array may contain duplicates.
"""

def search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if arr[middle] == target:
            return True
        
        if arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return False