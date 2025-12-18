"""
QUESTION:
Implement the bubble_sort function, which sorts an array of integers in ascending order without using any built-in sorting methods. The function should return the sorted array.
"""

def bubble_sort(arr):
    """
    Sorts an array of integers in ascending order using the bubble sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """

    len_arr = len(arr)

    for i in range(len_arr):
        for j in range(0, len_arr - i - 1):

            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr