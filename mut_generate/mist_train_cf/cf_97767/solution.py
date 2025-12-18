"""
QUESTION:
Write a Python function named `median` that calculates the median of a list of numbers. The list can contain any number of integers or floats between negative infinity and positive infinity. The function should return the median value of the input list.
"""

def calculate_median(lst):
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