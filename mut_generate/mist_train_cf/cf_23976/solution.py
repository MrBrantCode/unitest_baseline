"""
QUESTION:
Implement a function `binary_search` that takes a sorted list of integers and a target integer as input, and returns the index of the target element if found, or False if not found. The input list is guaranteed to be sorted.
"""

def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] < target:
            low = mid + 1
        elif list[mid] > target:
            high = mid - 1
        else:
            return mid
    return False