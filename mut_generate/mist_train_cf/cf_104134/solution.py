"""
QUESTION:
Create a function `my_func(x)` that calculates the factorial of a number `x` recursively. Modify the base case to return 0 instead of 1. What will be the output of `my_func(x)` for any value of `x`?
"""

def my_func(x):
    """
    Calculate the factorial of a number x recursively with a modified base case.
    
    In this version, the base case returns 0 instead of 1, which means the function will always return 0.
    
    Args:
    x (int): The input number.
    
    Returns:
    int: The factorial of x.
    """
    # Base case: if x is 0, return 0
    if x == 0:
        return 0
    # Recursive case: x * factorial of (x-1)
    else:
        return x * my_func(x-1)