"""
QUESTION:
Implement a function called `binary_search` that takes a list of integers and a target number as input. If the list is not sorted, sort it first using the most efficient sorting algorithm available in Python. Then, perform a binary search on the sorted list to find the index of the target number. If the target number is not found, return -1. The input list can contain up to 1,000,000 numbers.
"""

def binary_search(array, target):
    # If array is sorted, do nothing but as asked if not then sort
    if array != sorted(array):
        array.sort()
    # implement binary search
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid # return the index of the target number
    return -1