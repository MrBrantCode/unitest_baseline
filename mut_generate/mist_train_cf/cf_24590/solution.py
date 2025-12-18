"""
QUESTION:
Implement the QuickSort function, a divide and conquer algorithm that takes a list of integers as input and returns a sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def quick_sort(arr):
    """
    Sorts a list of integers using the QuickSort algorithm.

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
    return quick_sort(left) + middle + quick_sort(right)