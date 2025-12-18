"""
QUESTION:
Write a function `sum_elements(data)` that takes a list of at least 3 and at most 10 non-negative integers as input and returns the sum of all the elements in the list using recursion.
"""

def sum_elements(data):
    """
    This function calculates the sum of all non-negative elements in a list using recursion.
    
    Args:
    data (list): A list of non-negative integers with a length between 3 and 10 (inclusive).
    
    Returns:
    int: The sum of all non-negative elements in the list.
    """
    
    # base case: if the list is empty, return 0
    if len(data) == 0:
        return 0
    
    # if the first element is negative, skip it and sum the rest of the list
    elif data[0] < 0:
        return sum_elements(data[1:])
    
    # if the first element is non-negative, add it to the sum of the rest of the list
    else:
        return data[0] + sum_elements(data[1:])