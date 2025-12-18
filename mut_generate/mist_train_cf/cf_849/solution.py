"""
QUESTION:
Create a function `squaring_result` that takes an integer `x` as input and returns the result based on the following conditions:
- If `x` is less than 0, return -1.
- If `x` is 0, 1, 2, 3, 4, 5, 6, or 7, return `x` squared.
- If `x` is greater than 7, return `x` squared.
Minimize the number of logical steps in the solution.
"""

def squaring_result(x):
    """
    Returns the result of squaring x or -1 based on conditions.
    
    If x is less than 0, return -1.
    If x is 0, 1, 2, 3, 4, 5, 6, or 7, return x squared.
    If x is greater than 7, return x squared.
    
    Parameters:
    x (int): The input number.
    
    Returns:
    int: The result based on the conditions.
    """
    return x ** 2 if x >= 0 else -1