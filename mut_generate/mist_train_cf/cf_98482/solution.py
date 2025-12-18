"""
QUESTION:
Write a function `apply_to_all_but_last_two` that applies a given function to all elements of a list except the last two sublists, resulting in a nested list of tuples as the output. The input function should take one argument and return one value. The list input to the function will contain at least two sublists.
"""

def apply_to_all_but_last_two(lst, func):
    """
    Applies a given function to all elements of a list except the last two sublists.

    Args:
        lst (list): A list containing at least two sublists.
        func (function): A function that takes one argument and returns one value.

    Returns:
        list: A nested list of tuples.
    """
    return list(map(func, lst[:-2]))