"""
QUESTION:
Write a function named 'assign_x_to_y' that assigns the value of variable x to variable y using only bitwise operators. The function should not use any arithmetic operators or assignment operators (such as = or +=) and should have a time complexity of O(1) and a space complexity of O(1).
"""

def assign_x_to_y(x, y):
    """
    Assigns the value of variable x to variable y using only bitwise operators.

    Args:
        x (int): The value to be assigned.
        y (int): The variable to be assigned to.

    Returns:
        int: The assigned value.
    """
    return (y & 0) ^ (x ^ y)