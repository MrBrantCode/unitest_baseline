"""
QUESTION:
Implement a function named `append_elem` that takes a list and an optional integer as parameters and appends the integer to the list. The integer parameter should default to 1 if not provided. The function should return the updated list. 

Restriction: The function should handle mutable list objects and demonstrate how Python's call-by-object sharing strategy affects the outcome.
"""

def append_elem(lst, elem=1):
    """
    Appends the given element (which defaults to 1) to the given list.
    
    Args:
    lst (list): The list to append the element to.
    elem (int): The element to append. Defaults to 1.
    
    Returns:
    list: The updated list.
    """
    lst.append(elem)
    return lst