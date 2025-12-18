"""
QUESTION:
Create a function called `add_without_plus` that takes two integers as input and returns their sum without using the '+' operator. Implement the function using bitwise operations.
"""

def add_without_plus(x, y):
    """
    This function adds two integers without using the '+' operator.
    
    Parameters:
    x (int): The first integer to be added.
    y (int): The second integer to be added.
    
    Returns:
    int: The sum of the two integers.
    """
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x