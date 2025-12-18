"""
QUESTION:
Implement a function named `find_unique_elements` that takes a list of integers as input and returns a new list containing only the unique elements from the input list, preserving their original order. Do not use any built-in functions or libraries. The input list may contain negative integers.
"""

def find_unique_elements(lst):
    """
    Returns a new list containing only the unique elements from the input list, 
    preserving their original order.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A list of unique integers.
    """
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst