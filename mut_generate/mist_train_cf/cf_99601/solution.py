"""
QUESTION:
Implement the binary_search function that takes a sorted array of integers and a target value as input, and returns the index of the target value in the array. The function should use the binary search algorithm, which repeatedly divides the search interval in half until the target value is found or the search interval is empty. If the target value is not found, the function should return -1. Assume the input array is sorted in ascending order and the target value is an integer.
"""

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1