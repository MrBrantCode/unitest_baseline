"""
QUESTION:
Implement a function `quicksort(arr)` that recursively sorts a given list of integers using the quicksort algorithm, without using built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and a space complexity of O(log n).
"""

def quicksort(arr):
    """
    Recursively sorts a given list of integers using the quicksort algorithm.

    Args:
        arr (list): The input list of integers.

    Returns:
        list: The sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)