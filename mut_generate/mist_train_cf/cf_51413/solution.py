"""
QUESTION:
Create a function `filter_greater_than_50` that takes a list of integers as input and returns a new list containing only the elements that are less than or equal to 50.
"""

def filter_greater_than_50(num_list):
    """
    This function filters a list of integers to include only the elements less than or equal to 50.
    
    Args:
    num_list (list): A list of integers.
    
    Returns:
    list: A new list containing only the elements that are less than or equal to 50.
    """
    return [i for i in num_list if i <= 50]