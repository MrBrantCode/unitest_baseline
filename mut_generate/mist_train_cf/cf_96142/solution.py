"""
QUESTION:
Implement a function `bubble_sort` that takes a list of numbers as input, sorts the list in ascending order using the bubble sort algorithm, and returns the sorted list. The function should not use any built-in sorting functions or methods. The input list contains only integers, and the function should handle lists of any length.
"""

def bubble_sort(n_list):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    Args:
    n_list (list): A list of integers to be sorted.

    Returns:
    list: The sorted list in ascending order.
    """
    n = len(n_list)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if n_list[j] > n_list[j+1]:
                n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
                swapped = True
        if not swapped:
            break
    return n_list