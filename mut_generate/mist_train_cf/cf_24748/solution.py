"""
QUESTION:
Implement a function called `bubbleSort` that sorts an array of integers in ascending order using the bubble sort algorithm. The input array is unsorted and contains distinct integers. The function should return the sorted array. The function should not use any built-in sorting functions.
"""

def bubble_sort(arr):
    """
    Sorts an array of integers in ascending order using the bubble sort algorithm.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The sorted array.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr