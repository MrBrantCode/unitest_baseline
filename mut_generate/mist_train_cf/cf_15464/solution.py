"""
QUESTION:
Write a function named `remove_negatives_and_sort` that takes a list of integers as input, removes any negative numbers from the list, removes any duplicate elements, and sorts the list in ascending order. The function should return the modified list.
"""

def remove_negatives_and_sort(lst):
    """
    Removes negative numbers from the list, removes any duplicate elements, 
    and sorts the list in ascending order.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The modified list.
    """
    return sorted(list(set([num for num in lst if num >= 0])))