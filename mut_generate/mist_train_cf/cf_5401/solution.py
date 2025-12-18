"""
QUESTION:
Create a function named `insertion_sort_descending` that performs insertion sorting on a given list of integers in descending order. The function should take a list of integers as input and return the sorted list. The function should not use any built-in sorting functions and should have a time complexity of O(n^2), where n is the number of elements in the list.
"""

def insertion_sort_descending(lst):
    """
    Sorts a list of integers in descending order using the insertion sort algorithm.

    Args:
        lst (list): A list of integers to be sorted.

    Returns:
        list: The sorted list in descending order.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key > lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst