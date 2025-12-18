"""
QUESTION:
Create a function called `binary_search_recursive` that performs a recursive binary search in a sorted array. The function should take four parameters: a sorted array `arr`, a target element `target`, a start index `start`, and an end index `end`. The function should return the index of the target element if found, or -1 if the target is not present. The time complexity of the function should be O(log n).
"""

def binary_search_recursive(arr, target, start, end):
    """
    Recursive binary search function.

    Parameters:
    arr (list): A sorted array.
    target: The target element to search for.
    start (int): The start index of the search range.
    end (int): The end index of the search range.

    Returns:
    int: The index of the target element if found, or -1 if not present.
    """
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, end)