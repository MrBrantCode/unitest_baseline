"""
QUESTION:
Create a function that models the relationship between three variables x, y, and z, where y is directly proportional to x and inversely proportional to z. The function should take x and z as inputs and return y. The relationship can be described by the equation y = a*x = b/z, where a and b are constants. Assume that the relationship is strictly proportional or inversely proportional with no added constant term.
"""

def calculate_y(x, z, a, b):
    """
    Calculate y based on the relationship y = a*x = b/z.

    Args:
        x (float): The direct proportionality variable.
        z (float): The inverse proportionality variable.
        a (float): The proportionality constant with x.
        b (float): The proportionality constant with z.

    Returns:
        float: The calculated y value.
    """
    return (a * x) if z != 0 else float('inf')