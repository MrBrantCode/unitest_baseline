"""
QUESTION:
Implement a binary search function named `binary_search` that takes a sorted list of integers and a target number as input, and returns the index of the target number in the list. If the target number is not found, return -1. The function should have a time complexity of O(log n) and be able to handle a list of up to 1 million integers.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1