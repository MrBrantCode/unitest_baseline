"""
QUESTION:
Design a function named `search` that searches for a target element in a sorted array with a time complexity of O(log n) without using any built-in search functions or libraries. The array may contain duplicate elements, and the function should return True if the target element is found and False otherwise. The function takes a sorted array `arr` and a target element `target` as input and does not use any additional space that scales with the input size.
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