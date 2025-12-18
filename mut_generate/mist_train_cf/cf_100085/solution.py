"""
QUESTION:
Write a function named `median` that takes a list of numbers as input and returns the median value of the list. The function should handle both lists with an even and an odd number of elements, and the input list is expected to contain floating point numbers between 0 and 100.
"""

def median(lst):
    """
    This function takes a list of numbers as input and returns the median value of that list.
    """
    sorted_lst = sorted(lst)
    lst_len = len(lst)
    mid = lst_len // 2
    if lst_len % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]