"""
QUESTION:
Write a function `second_derivative` to find the second derivative of a polynomial function f(x) = ax^n, where 'a' and 'n' are constants, without using any external libraries or calculus. The function should return a string representing the second derivative in the format 'f''(x) = bx^m', where 'b' is the coefficient and 'm' is the exponent.
"""

def second_derivative(a, n):
    """
    This function calculates the second derivative of a polynomial function f(x) = ax^n.
    
    Parameters:
    a (int): The coefficient of the polynomial function.
    n (int): The exponent of the polynomial function.
    
    Returns:
    str: A string representing the second derivative in the format 'f''(x) = bx^m'.
    """
    # Calculate the coefficient of the first derivative
    first_derivative_coefficient = a * n
    
    # Calculate the exponent of the first derivative
    first_derivative_exponent = n - 1
    
    # Calculate the coefficient of the second derivative
    second_derivative_coefficient = first_derivative_coefficient * first_derivative_exponent
    
    # Calculate the exponent of the second derivative
    second_derivative_exponent = first_derivative_exponent - 1
    
    # Return the second derivative as a string
    return f"f''(x) = {second_derivative_coefficient}x^{second_derivative_exponent}"