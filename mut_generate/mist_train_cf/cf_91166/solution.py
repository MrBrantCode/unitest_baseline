"""
QUESTION:
Write a function `sort_and_swap_largest` that takes a list of integers as input, sorts it in ascending order, and then swaps the two largest elements. The function should return the modified list. The list contains at least two distinct elements.
"""

def sort_and_swap_largest(lst):
    """
    Sorts a list of integers in ascending order and swaps the two largest elements.
    
    Args:
        lst (list): A list of integers with at least two distinct elements.
    
    Returns:
        list: The modified list with the two largest elements swapped.
    """
    # Sorting the list in ascending order
    sorted_lst = sorted(lst)
    
    # Swapping the two largest elements
    sorted_lst[-1], sorted_lst[-2] = sorted_lst[-2], sorted_lst[-1]
    
    return sorted_lst