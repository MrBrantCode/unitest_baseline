"""
QUESTION:
Write a function named bubble_sort that takes a list of positive integers as input, sorts the list in ascending order using the Bubble Sort algorithm, and returns the sorted list along with the number of comparisons and swaps performed. The function should maintain the relative order of equal elements and have a time complexity of O(n^2).
"""

def bubble_sort(arr):
    """
    Sorts a list of positive integers using the Bubble Sort algorithm.

    Args:
    arr (list): A list of positive integers.

    Returns:
    tuple: A tuple containing the sorted list, number of comparisons, and number of swaps.
    """
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return arr, comparisons, swaps