"""
QUESTION:
Design a function `binary_search_handle_duplicates_unsorted` that performs a binary search on a list to find all instances of a target element. The function should first sort the list in ascending order if it's not already sorted, and then find the indices of all instances of the target element. If the target element is not found, the function should return 'Not Found'. The function should have a time complexity of O(n log n) or better.
"""

def binary_search_handle_duplicates_unsorted(arr, target):
    arr.sort()
    indices = [i for i, x in enumerate(arr) if x == target]
    return indices if indices else 'Not Found'