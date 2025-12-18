"""
QUESTION:
Implement the `bubble_sort` function to sort a list of float numbers in ascending order using the Bubble Sort algorithm without using any built-in sorting functions or libraries. The function should have a time complexity of O(n^2) or better.
"""

def bubble_sort(arr):
    """
    Sorts a list of float numbers in ascending order using the Bubble Sort algorithm.

    Args:
    arr (list): A list of float numbers.

    Returns:
    list: The sorted list of float numbers.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr