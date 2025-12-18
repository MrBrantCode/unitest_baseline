"""
QUESTION:
Implement the quicksort function, which sorts a list of elements using the quicksort algorithm. The function should take one argument, the list to be sorted, and return the sorted list. Ensure that the function's spatial complexity is considered in its implementation.
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