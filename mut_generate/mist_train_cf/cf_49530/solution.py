"""
QUESTION:
Write a function named `binary_search` that takes in a sorted array and a target value as input and returns the index of the target value in the array if found, or -1 if not found. The array is sorted in ascending order and can contain duplicate values.
"""

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1