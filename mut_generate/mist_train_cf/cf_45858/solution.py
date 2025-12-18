"""
QUESTION:
Write a function called `sort_by_length` that rearranges the elements of a given array based on the length of each element. The function should take a list of strings as input and return the sorted list. The list should be sorted in ascending order by default, but should also be able to be sorted in descending order when a reverse parameter is set to True.
"""

def sort_by_length(arr, reverse=False):
    """
    Sorts a list of strings based on the length of each element.

    Args:
    arr (list): A list of strings.
    reverse (bool): An optional parameter to sort in descending order. Defaults to False.

    Returns:
    list: The sorted list of strings.
    """
    arr.sort(key=len, reverse=reverse)
    return arr