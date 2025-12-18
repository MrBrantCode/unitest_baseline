"""
QUESTION:
Write a function `ternary_condition` that takes an integer `x` as input and returns an integer `y`. The value of `y` should be -1 if `x` is less than 0, and the value of `z` should be 2 if `x` is equal to 0 or 3 if `x` is greater than 0. The solution must be implemented using a ternary operator in a single line of code, have a time complexity of O(1), and not use any temporary variables.
"""

def ternary_condition(x):
    """
    Returns an integer based on the value of x.
    
    If x is less than 0, returns -1.
    If x is equal to 0, returns 2.
    If x is greater than 0, returns 3.
    
    Parameters:
    x (int): The input integer.
    
    Returns:
    int: The output integer based on the value of x.
    """
    return -1 if x < 0 else 2 if x == 0 else 3