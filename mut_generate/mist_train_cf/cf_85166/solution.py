"""
QUESTION:
Write a function called `solve_linear_equation` to isolate and identify the value of the variable 'x' in a simple linear equation of the form ax + b = c, where a, b, and c are constants. The function should take the coefficients a, b, and c as input and return the value of x.
"""

def solve_linear_equation(a, b, c):
    """
    This function isolates and identifies the value of the variable 'x' in a simple linear equation of the form ax + b = c.

    Parameters:
    a (float): The coefficient of x.
    b (float): The constant on the left side of the equation.
    c (float): The constant on the right side of the equation.

    Returns:
    float: The value of x.
    """
    # Subtract b from both sides to get ax = c - b
    # Then divide both sides by a to get x = (c - b) / a
    return (c - b) / a