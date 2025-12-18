"""
QUESTION:
Design a function `binary_search(arr, target)` that searches for a specified item `target` in a sorted list `arr` and returns the index of the first occurrence. If the item is not found in the list, the function should return -1. The function should be able to handle lists containing duplicate elements and have a time complexity of O(log n) for searching, where n is the number of elements in the list.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            result = mid
            high = mid - 1 
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return result