"""
QUESTION:
Write a function `solve_linear_equation(equation)` that solves a simple linear equation in the format "ax + b = c" or "ax - b = c", where 'a', 'b', and 'c' are integers (positive or negative). The function should return the numerical value of 'x'.
"""

def solve_linear_equation(equation):
    """
    Solves a simple linear equation in the format "ax + b = c" or "ax - b = c".

    Args:
    equation (str): A string representing the linear equation.

    Returns:
    float: The numerical value of 'x' in the equation.
    """
    equation_parts = equation.split()

    a = int(equation_parts[0][:-1])
    operation = equation_parts[1]
    b = int(equation_parts[2])
    c = int(equation_parts[4])

    if operation == '+':
        x = (c - b) / a
    else:
        x = (c + b) / a

    return x