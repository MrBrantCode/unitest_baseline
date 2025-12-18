"""
QUESTION:
Implement a function `quicksort` that sorts a list of elements using the quicksort algorithm. The function should take a list as input and return the sorted list.
"""

def quicksort(arr):
    """
    Sorts a list of elements using the quicksort algorithm.

    Args:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)