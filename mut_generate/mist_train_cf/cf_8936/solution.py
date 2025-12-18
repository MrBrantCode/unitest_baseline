"""
QUESTION:
Create a list comprehension function that takes a list of integers as input and returns a new list. The new list should contain doubled elements if the corresponding element in the input list is odd, and squared elements if the corresponding element is even.
"""

def transform_list(lst):
    """
    This function takes a list of integers as input and returns a new list.
    The new list contains doubled elements if the corresponding element in the input list is odd, 
    and squared elements if the corresponding element is even.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A new list with transformed elements.
    """
    return [x*2 if x%2 != 0 else x**2 for x in lst]