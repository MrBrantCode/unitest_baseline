"""
QUESTION:
Write a recursive function called `square_even_elements` that takes a list of integers as input. The function should return a new list containing the squared values of only the even elements from the original list, while the odd elements are ignored. Use list comprehensions to achieve this result.
"""

def square_even_elements(lst):
    """
    This function takes a list of integers as input, squares the even elements, 
    and returns them in a new list while ignoring the odd elements.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list containing the squared values of the even elements.
    """
    if not lst:
        return []
    else:
        first_element = [lst[0]**2] if lst[0] % 2 == 0 else []
        return first_element + square_even_elements(lst[1:])