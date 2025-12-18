"""
QUESTION:
Implement a function `quicksort` that sorts a list of elements in ascending order using the quicksort algorithm.
"""

def quicksort(arr):
    """
    This function sorts a list of elements in ascending order using the quicksort algorithm.

    Parameters:
    arr (list): A list of elements to be sorted

    Returns:
    list: A sorted list of elements in ascending order
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)