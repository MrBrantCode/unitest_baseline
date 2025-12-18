"""
QUESTION:
Write a function `squaredValues(lst)` that calculates the sum of the squares of only the even integers in a given list `lst`. The function should handle cases where the input list contains non-integer values.
"""

def sum_even_squares(lst):
    """
    Calculate the sum of the squares of only the even integers in a given list.
    
    Args:
    lst (list): A list of integers and/or non-integer values.
    
    Returns:
    int: The sum of the squares of the even integers in the list.
    """
    result = 0
    for i in lst:
        if isinstance(i, int) and i % 2 == 0:
            result += i ** 2
    return result