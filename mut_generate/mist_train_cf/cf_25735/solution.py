"""
QUESTION:
Implement a function `evaluate_quadratic_expression` that calculates the value of a quadratic expression $ax^2 + bx + c$ given the coefficients $a$, $b$, $c$, and the value of $x$. The function should return the calculated value.
"""

def evaluate_quadratic_expression(a, b, c, x):
    """
    Calculates the value of a quadratic expression ax^2 + bx + c.
    
    Args:
        a (float): The coefficient of x^2.
        b (float): The coefficient of x.
        c (float): The constant term.
        x (float): The value of x.
    
    Returns:
        float: The calculated value of the quadratic expression.
    """
    return a * x**2 + b * x + c