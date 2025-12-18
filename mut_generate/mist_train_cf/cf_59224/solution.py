"""
QUESTION:
Create a function named `sort_sublists` that sorts a list of sublists in descending order based on the secondary elements of each sublist. The input is a list of sublists where each sublist has at least two elements. The function should return the sorted list.
"""

def sort_sublists(lst):
    """
    Sorts a list of sublists in descending order based on the secondary elements of each sublist.

    Args:
        lst (list): A list of sublists where each sublist has at least two elements.

    Returns:
        list: The sorted list of sublists.
    """
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst