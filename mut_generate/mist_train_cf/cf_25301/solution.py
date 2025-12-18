"""
QUESTION:
Implement a function named `quick_sort` to sort a list of integers using the QuickSort algorithm with the best time complexity of O(nlog(n)).
"""

def quick_sort(arr):
    """
    Sorts a list of integers using the QuickSort algorithm.

    Args:
    arr (list): The list of integers to be sorted.

    Returns:
    list: The sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)