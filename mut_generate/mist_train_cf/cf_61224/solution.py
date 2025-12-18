"""
QUESTION:
Write a function `double_the_difference` that takes a list of numbers as input and returns the sum of the squares of the odd positive integers in the list. Ignore non-integer and negative numbers. If the input list is empty, return 0.
"""

def double_the_difference(lst):
    """
    Returns the sum of the squares of the odd positive integers in the list.
    Ignores non-integer and negative numbers. If the input list is empty, returns 0.
    
    Parameters:
    lst (list): A list of numbers.
    
    Returns:
    int: The sum of the squares of the odd positive integers in the list.
    """
    return sum([i**2 for i in lst if isinstance(i, int) and i > 0 and i % 2 == 1])