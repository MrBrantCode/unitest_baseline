"""
QUESTION:
Write a function `sort_sublists` that takes a list of lists as input, where each sublist has at least three elements. The function should sort the list of lists first by the second element of each sublist in descending order, and then by the third element in ascending order if there are multiple sublists with the same second element. The input list can contain up to 10^5 elements.
"""

def sort_sublists(lst):
    """
    Sorts a list of lists by the second element in descending order, 
    and then by the third element in ascending order if there are multiple sublists with the same second element.

    Args:
        lst (list): A list of lists, where each sublist has at least three elements.

    Returns:
        list: The sorted list of lists.
    """
    lst.sort(key=lambda x: (-x[1], x[2]))
    return lst