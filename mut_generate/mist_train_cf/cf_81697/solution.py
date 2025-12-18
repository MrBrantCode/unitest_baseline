"""
QUESTION:
Create a function `filter_above_limit` that takes a list of integers as input and returns a new list containing only the elements that are greater than or equal to 20.
"""

def filter_above_limit(num_array):
    """
    This function takes a list of integers as input and returns a new list containing only the elements that are greater than or equal to 20.
    
    Args:
    num_array (list): A list of integers.
    
    Returns:
    list: A new list containing only the elements that are greater than or equal to 20.
    """
    return [i for i in num_array if i >= 20]