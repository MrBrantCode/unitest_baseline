"""
QUESTION:
Create a function named `binary_search` that implements a binary search algorithm. The function should take two parameters: `arr` (a sorted list) and `goal` (the value to search for). The function should return the index of `goal` if it is present in the list, or -1 if it is not found.
"""

def entance(arr, goal):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == goal:
            return mid
        elif arr[mid] < goal:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1