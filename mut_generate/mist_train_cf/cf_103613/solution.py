"""
QUESTION:
Create a function named `binary_search` that takes in a sorted list `arr` and a value `goal` as parameters. Implement a binary search algorithm to find the index of `goal` in `arr`. If `goal` is found, return its index; otherwise, return -1. The input list `arr` is guaranteed to be sorted.
"""

def binary_search(arr, goal):
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