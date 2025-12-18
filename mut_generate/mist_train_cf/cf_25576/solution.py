"""
QUESTION:
Implement a function named `partition` and `quicksort` to sort an array of integers using the quicksort algorithm. The function `partition` should rearrange the array such that all elements less than the pivot are on the left of it and all elements greater are on the right. The function `quicksort` should recursively call itself to sort the sub-arrays on either side of the pivot. The array is 0-indexed and the `quicksort` function should sort the array in-place.
"""

def partition(array, low, high):
    """
    Rearrange the array such that all elements less than the pivot are on the left of it 
    and all elements greater are on the right.

    Args:
        array (list): The input list of integers.
        low (int): The starting index of the sub-array.
        high (int): The ending index of the sub-array.

    Returns:
        int: The index of the pivot element.
    """
    pivot = array[high]
    i = low - 1 
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quicksort(array, low, high):
    """
    Sort the array in-place using the quicksort algorithm.

    Args:
        array (list): The input list of integers.
        low (int): The starting index of the sub-array.
        high (int): The ending index of the sub-array.
    """
    if low < high:
        pivot_position = partition(array, low, high)
        quicksort(array, low, pivot_position-1)
        quicksort(array, pivot_position+1, high)