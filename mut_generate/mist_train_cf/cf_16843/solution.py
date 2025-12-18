"""
QUESTION:
Write a function `find_max_number` that takes three integers as input and returns the maximum of the three numbers.
"""

def find_max_number(x, y, z):
    """
    This function takes three integers as input and returns the maximum of the three numbers.
    
    Args:
    x (int): The first number.
    y (int): The second number.
    z (int): The third number.
    
    Returns:
    int: The maximum of the three numbers.
    """
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return "All numbers are equal"