"""
QUESTION:
Write a function `sort_sublists` that sorts a given list of sublists in ascending order. The sorting criteria should be the product of the elements in each sublist. If two sublists have the same product, they should be sorted based on the sum of their elements. If both the product and sum are the same, they should be sorted lexicographically.
"""

def sort_sublists(sublists):
    """
    Sorts a given list of sublists in ascending order based on the product of their elements.
    If two sublists have the same product, they are sorted based on the sum of their elements.
    If both the product and sum are the same, they are sorted lexicographically.

    Args:
        sublists (list): A list of sublists.

    Returns:
        list: A sorted list of sublists.
    """
    return sorted(sublists, key=lambda x: (tuple(sorted(x)), sum(x), tuple(x)))