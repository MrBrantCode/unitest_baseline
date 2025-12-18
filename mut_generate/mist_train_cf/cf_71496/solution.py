"""
QUESTION:
Implement a binary search function called `binary_search` that takes in a sorted list `data` and a target value `target` and returns a boolean indicating whether the target is present in the list. Assume that the input list is sorted in ascending order.
"""

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        if target == data[middle]: # check if target is present at mid
            return True
        elif target < data[middle]: # If target is greater, ignore left half
            high = middle - 1
        else: # If target is smaller, ignore right half
            low = middle + 1
    return False # if element is not present