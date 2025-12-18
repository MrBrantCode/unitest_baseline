"""
QUESTION:
Write a function `ternary_operator` that takes an integer `x` as input and returns an integer value based on the following conditions: 
- if `x` is greater than 0, return 10
- if `x` is less than -5, return 0
- otherwise, return 5.
"""

def ternary_operator(x):
    """
    Returns an integer value based on the input integer x.
    
    If x is greater than 0, returns 10.
    If x is less than -5, returns 0.
    Otherwise, returns 5.
    
    Parameters:
    x (int): The input integer.
    
    Returns:
    int: The result based on the input x.
    """
    return 10 if x > 0 else (0 if x < -5 else 5)