"""
QUESTION:
Implement a function `binary_search` that performs a recursive binary search on a sorted list of integers to find the first occurrence of a target element. The function should take as input a sorted list `arr`, a target element `target`, and the lower and upper indices `low` and `high` of the current search range. The function should return the found element and its index, or `None` and `-1` if the element is not found.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return None, -1

    mid = (low + high) // 2

    if arr[mid] == target:
        index = find_first_occurrence(arr, target, low, mid)
        return arr[index], index
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

def find_first_occurrence(arr, target, low, high):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid
        else:
            low = mid + 1
    return low