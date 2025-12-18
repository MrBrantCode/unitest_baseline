"""
QUESTION:
Construct a function `quickSort` to implement the QuickSort algorithm. Implement the function using the divide-and-conquer strategy and ensure it can handle large datasets. The function should take one argument: a list of integers to be sorted. There are no restrictions on the input list, and the function should return the sorted list.
"""

def quickSort(arr):
    """
    Sorts a list of integers using the QuickSort algorithm.

    Args:
        arr (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)