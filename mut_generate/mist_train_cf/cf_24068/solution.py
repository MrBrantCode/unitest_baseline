"""
QUESTION:
Implement a function `bubble_sort` that takes an array of integers as input and returns the sorted array using the bubble sort algorithm. The array can contain duplicate elements and may be unsorted in either ascending or descending order. The function should be efficient in terms of time complexity and should modify the original array in-place.
"""

def bubble_sort(arr):
    """
    Sorts an array of integers using the bubble sort algorithm.

    Args:
        arr (list): The input array to be sorted.

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