"""
QUESTION:
Create a function to sort a list of elements in ascending order using Python's built-in sort() function. The function should take two parameters: the list to be sorted and a function (optional) that defines the sorting criteria. The function should return the sorted list and preserve the original positions of equal elements.
"""

def sort_list(input_list, key=None):
    """
    Sorts a list of elements in ascending order using Python's built-in sort() function.

    Args:
        input_list (list): The list to be sorted.
        key (function, optional): A function that defines the sorting criteria. Defaults to None.

    Returns:
        list: The sorted list.
    """
    if key is not None:
        input_list.sort(key=key)
    else:
        input_list.sort()
    return input_list