"""
QUESTION:
Write a Python function `find_derivative` that takes a polynomial function of the form f(x) = ax^2 + bx + c as input and returns its derivative f'(x). The function should take coefficients a, b, and c as input, and return the coefficients of the derivative in the form of a string "dx/dx = mx + n". Assume a, b, and c are integers and the derivative should be simplified.
"""

def find_derivative(a, b, c):
    """
    This function calculates the derivative of a polynomial function f(x) = ax^2 + bx + c.
    
    Args:
        a (int): The coefficient of x^2 in the polynomial function.
        b (int): The coefficient of x in the polynomial function.
        c (int): The constant term in the polynomial function.
    
    Returns:
        str: The derivative of the polynomial function in the form "dx/dx = mx + n".
    """
    # The derivative of x^2 is 2x, so the coefficient of x^2 in the derivative is 2a
    m = 2 * a
    # The derivative of x is 1, so the coefficient of x in the derivative is b
    n = b
    # Return the derivative as a string
    if m == 0:
        return f"dx/dx = {n}"
    elif n == 0:
        return f"dx/dx = {m}x"
    else:
        return f"dx/dx = {m}x + {n}"