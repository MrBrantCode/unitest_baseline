"""
QUESTION:
Write a function `append_element` that appends an element to a list and returns the modified list. The function should take two parameters: the original list and the element to be appended. The function should not create a new list, it should modify the original list. If a new variable is assigned the original list before the function call, the new variable should also be updated after the function call.
"""

def append_element(lst, element):
    """
    Appends an element to a list and returns the modified list.
    
    Args:
    lst (list): The original list to be modified.
    element: The element to be appended to the list.
    
    Returns:
    list: The modified list with the element appended.
    """
    lst.append(element)
    return lst