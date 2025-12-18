"""
QUESTION:
Implement a function `swap_first_and_last_elements` that takes a list of integers as input, swaps the places of the first and last elements, and returns the modified list. The function should not use any additional variables or built-in functions, have a time complexity of O(1), and not modify the original list.
"""

def swap_first_and_last_elements(lst):
    """
    This function takes a list of integers as input, swaps the places of the first and last elements, 
    and returns the modified list without using any additional variables or built-in functions.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The modified list with the first and last elements swapped.
    """
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst