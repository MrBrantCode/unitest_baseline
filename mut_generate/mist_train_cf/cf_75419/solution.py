"""
QUESTION:
Create a function `bubble_sort_descending` that sorts a list of integers in descending order without using any built-in sorting functions. The function should return the sorted list and the number of swaps performed.
"""

def bubble_sort_descending(lst):
    """
    Sorts a list of integers in descending order using bubble sort and returns the sorted list along with the number of swaps performed.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple: A tuple containing the sorted list and the number of swaps performed.
    """
    swaps = 0
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swaps += 1
    return lst, swaps