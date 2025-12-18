"""
QUESTION:
Determine the value of `x` when `y` is 13, given that `x` and `y` are directly proportional and `x = 3` when `y = 8`.
"""

def find_x(y):
    """
    Find the value of x when y is given, 
    given that x and y are directly proportional 
    and x = 3 when y = 8.

    Args:
    y (int or float): The value of y.

    Returns:
    int or float: The value of x.
    """
    # Determine the constant of proportionality
    k = 3 / 8
    
    # Use the constant of proportionality to find the new value of x
    x = k * y
    return x