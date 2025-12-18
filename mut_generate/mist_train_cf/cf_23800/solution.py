"""
QUESTION:
Write a function `quicksort` that takes a list of integers as input and returns a sorted list of integers. Implement a divide-and-conquer approach by selecting a pivot and partitioning the list into two sublists: one containing elements smaller than the pivot, and the other containing elements larger than the pivot. Recursively apply the same process to the sublists until the entire list is sorted.
"""

def quicksort(arr):
    """
    Sorts a list of integers using the quicksort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)