"""
QUESTION:
Given a function f(x,y) = (x + y)^3 + x^2 + y^2, write a function to calculate the result for given x and y values. The function should take two parameters, x and y, and return the calculated result. Calculate f(x,y) for x = 2 and y = 3.
"""

def f(x, y):
    """
    Calculate the result of f(x,y) = (x + y)^3 + x^2 + y^2.

    Args:
        x (int): The x value.
        y (int): The y value.

    Returns:
        int: The calculated result.
    """
    return (x + y)**3 + x**2 + y**2