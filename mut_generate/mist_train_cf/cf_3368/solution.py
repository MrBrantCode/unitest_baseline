"""
QUESTION:
Implement a function `bubble_sort_desc` that sorts an array of n integers in descending order using the bubble sort algorithm, while preserving the relative order of duplicate integers. The function should not take any additional arguments other than the input array.
"""

def bubble_sort_desc(arr):
    """
    Sorts an array of n integers in descending order using the bubble sort algorithm, 
    while preserving the relative order of duplicate integers.

    Args:
        arr (list): A list of integers to be sorted.

    Returns:
        list: The sorted list in descending order.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            elif arr[i] == arr[i+1]:
                # Since Python lists maintain the insertion order, 
                # we can compare the indices of the elements in the original list
                # to determine their relative order.
                if arr.index(arr[i]) < arr.index(arr[i+1]):
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
    return arr