"""
QUESTION:
Design a function `insertion_sort` that performs a binary search-based insertion sort on a list of integers. The function should take a list of integers as input, sort it using binary search-based insertion sort, and return the sorted list along with the total number of operations (comparisons and swaps) performed. The input list can contain positive, negative integers, and zeros.
"""

def insertion_sort(arr):
    """
    Sorts a list of integers using binary search-based insertion sort and returns the sorted list along with the total number of operations (comparisons and swaps) performed.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the sorted list and the total number of operations.
    """
    operations = 0
    for i in range(1, len(arr)):
        operations += 1  # for the comparison operation
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
        operations += len(arr[j:i]) * 2  # for the swaps
    return arr, operations


def binary_search(arr, val, start, end):
    """
    Performs a binary search on a sorted list to find the correct position for a value.

    Args:
        arr (list): A sorted list.
        val (int): The value to be inserted.
        start (int): The start index of the search range.
        end (int): The end index of the search range.

    Returns:
        int: The correct position for the value.
    """
    # we start by assuming the item is not found
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid