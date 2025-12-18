"""
QUESTION:
Assign the value of variable x to variable y using only bitwise operators without using arithmetic or assignment operators (such as = or +=). The variables x and y are initialized as x = 0 and y = 1. The function to achieve this should be able to take x and y as input and return the updated value of y.
"""

def assign_x_to_y(x, y):
    """
    Assign the value of x to y using only bitwise operators.
    
    Parameters:
    x (int): The value to be assigned.
    y (int): The variable to be updated.
    
    Returns:
    int: The updated value of y.
    """
    return (y & 0) | (x & 1)