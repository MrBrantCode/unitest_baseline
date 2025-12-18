"""
QUESTION:
Write a function called `sort_ascending` that sorts an array of integers in ascending order. The function should take an array of integers as input and return the sorted array. The array can contain any number of elements, and the elements can be any integer values, including negative numbers. Implement the sorting algorithm from scratch without using built-in sorting functions.
"""

def sort_ascending(arr):
    """
    Sorts an array of integers in ascending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(arr_length - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr