"""
QUESTION:
Write a function named `binary_search` that takes a sorted list of integers in ascending order and an integer element as input, and returns the correct index at which the element should be inserted to maintain the sorted order of the list. The list may contain duplicate elements.
"""

def binary_search(arr, element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return low