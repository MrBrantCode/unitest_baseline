"""
QUESTION:
Given an equation of the form y + x = z, write a function `solve_for_y` that solves for y and rounds the result to the nearest whole number. The function should take in the values of x and z as parameters.
"""

def solve_for_y(x, z):
    """
    Solves for y in the equation y + x = z and rounds the result to the nearest whole number.

    Args:
        x (float): The value of x in the equation.
        z (float): The value of z in the equation.

    Returns:
        int: The value of y rounded to the nearest whole number.
    """
    return round(z - x)