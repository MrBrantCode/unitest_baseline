"""
QUESTION:
Implement a function `sort_descending(arr)` that takes an array of integers as input and sorts it in descending order using a custom algorithm. The algorithm should iterate over the array, comparing adjacent elements and swapping them if they are in ascending order. The function should return the sorted array.
"""

def sort_descending(arr):
    """
    Sorts the given array in descending order using a custom algorithm.

    Args:
    arr (list): A list of integers.

    Returns:
    list: The sorted array in descending order.
    """

    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr