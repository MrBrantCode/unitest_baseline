"""
QUESTION:
Create a function named `find_median` that takes a list of numbers as input and returns the median value. The input list may contain any number of elements. The function should handle both even and odd number of elements in the list.
"""

def find_median(lst):
    """
    This function finds the median value in a list of numbers.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The median value of the list.
    """
    sorted_lst = sorted(lst)
    lst_length = len(sorted_lst)
    if lst_length % 2 == 1:
        return sorted_lst[lst_length // 2]
    else:
        return (sorted_lst[lst_length // 2 - 1] + sorted_lst[lst_length // 2]) / 2