"""
QUESTION:
Write a function called `apply_to_all_except_last_two` that takes a list of elements and applies a given function to all elements of the list except the last two. The function should return a new list of tuples, where each tuple contains the original element and the result of applying the given function to the element.
"""

def apply_to_all_except_last_two(lst, func):
    """
    Applies a given function to all elements of the list except the last two.
    
    Args:
        lst (list): The input list of elements.
        func (function): The function to be applied to the elements.
    
    Returns:
        list: A new list of tuples, where each tuple contains the original element and the result of applying the given function to the element.
    """
    return list(map(lambda x: (x, func(x)), lst[:-2]))