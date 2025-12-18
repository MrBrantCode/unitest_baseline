"""
QUESTION:
Implement a function named `insertion_sort` that takes a list of integers as input and returns the sorted list using the Insertion Sort algorithm. The function should have a time complexity of O(n^2) in the worst case.
"""

def insertion_sort(arr):
    """
    Sorts a list of integers using the Insertion Sort algorithm.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr