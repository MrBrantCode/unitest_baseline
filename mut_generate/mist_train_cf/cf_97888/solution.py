"""
QUESTION:
Write a function named `binary_search` that implements the binary search algorithm to find the index of a target value in a sorted array of integers. The function should take two parameters: `array` and `target`, where `array` is a sorted list of integers and `target` is the value to search for. The function should return the index of the target value in the array, or -1 if the target value is not found. The function should use the binary search algorithm, repeatedly dividing the search interval in half until the target value is found or the search interval is empty.
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