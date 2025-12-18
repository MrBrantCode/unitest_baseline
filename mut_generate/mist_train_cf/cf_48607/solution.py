"""
QUESTION:
Implement a function named 'quick_sort' that sorts an array using the QuickSort algorithm. The function should take a list of integers as input and return the sorted list. The function should use the divide-and-conquer approach, including partitioning, recursion, and merging. Consider the impact of different pivot selection strategies on the algorithm's performance.
"""

def quick_sort(arr):
    """
    Sorts an array using the QuickSort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)