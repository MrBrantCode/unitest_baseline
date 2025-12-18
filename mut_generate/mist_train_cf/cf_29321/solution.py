"""
QUESTION:
Implement a function named `binary_search` that performs a binary search on a sorted list of integers. The function should take three parameters: a sorted list of integers `index`, the integer `target` to search for, and an optional parameter `end` to specify the end index for the search. If `end` is not provided, the search should consider the entire list. The function should return the index of the `target` integer in the `index` list, or -1 if it is not found within the specified range.
"""

def binary_search(index, target, end=None):
    start = 0
    if end is None:
        end = len(index)

    while start < end:
        mid = (start + end) // 2
        if index[mid] == target:
            return mid
        elif index[mid] < target:
            start = mid + 1
        else:
            end = mid
    return -1