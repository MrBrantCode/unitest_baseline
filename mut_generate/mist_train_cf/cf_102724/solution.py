"""
QUESTION:
Create a function `my_func(x)` that calculates the factorial of a given number `x` with a modified base case. The base case should return 0 when `x` equals 0, instead of the traditional 1. What will be the output of `my_func(x)` when `x` equals 5?
"""

def my_func(x):
    """
    This function calculates the factorial of a given number x.
    It has a modified base case that returns 0 when x equals 0, 
    instead of the traditional 1.
    
    Parameters:
    x (int): The number for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of x.
    """
    if x == 0:
        return 0
    else:
        return x * my_func(x-1)