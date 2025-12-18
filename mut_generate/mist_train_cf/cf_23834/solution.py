"""
QUESTION:
Write a function `select_last_two_elements` that takes a list as input and returns a new list containing the last two elements of the input list. The function should work for lists of any length, including lists with less than two elements, and should not modify the original list.
"""

def select_last_two_elements(mylist):
    """
    Returns a new list containing the last two elements of the input list.
    
    Args:
        mylist (list): The input list.
    
    Returns:
        list: A new list containing the last two elements of the input list.
    """
    return mylist[-2:]