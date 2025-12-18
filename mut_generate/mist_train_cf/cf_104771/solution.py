"""
QUESTION:
Implement a function called `binary_search` that takes a sorted list of distinct numbers in ascending order and a target number as input, and returns the index of the target number if found, and -1 otherwise.
"""

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if lst[mid] == target:
            return mid
        
        if lst[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1