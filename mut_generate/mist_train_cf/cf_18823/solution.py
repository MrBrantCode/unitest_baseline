"""
QUESTION:
Write a function `remove_third_element` that takes a list of at most 10 strings as input, removes the third element, and returns the modified list. If the list is empty or has less than 3 elements, return an error message. The function should achieve this in O(1) time complexity for the removal step and not use any built-in list manipulation functions or methods.
"""

def remove_third_element(lst):
    if len(lst) == 0:
        return "Error: The list is empty."
    elif len(lst) <= 2:
        return "Error: The list does not have a third element."
    
    lst[2] = None
    lst = [x for x in lst if x is not None]
    return lst