"""
QUESTION:
Implement the `binary_search` function to find the index of a target value in a sorted array of integers. The function should take two arguments: `array` and `target`. The function should return the index of the target value if found, or -1 if not found. The array is sorted in ascending order and contains unique elements. The function should use the binary search algorithm to find the target value.
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