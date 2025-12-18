"""
QUESTION:
Write a function `derivative_and_integral(xs, C)` that takes a list `xs` of coefficients representing a polynomial and a constant `C`. The function should return the derivative and integral of the polynomial, including the constant `C`, in a similar format. However, it should first perform a validity check on the input polynomial and constant. 

A valid polynomial must have at least one term and all coefficients must be integers. The constant `C` must also be an integer. If either the polynomial or the constant is invalid, the function should return an error message.
"""

def derivative_and_integral(xs, C):
    """
    This function calculates the derivative and integral of a polynomial, 
    including a constant C. It first checks the validity of the input polynomial 
    and constant. A valid polynomial must have at least one term and all coefficients 
    must be integers. The constant C must also be an integer.

    Args:
        xs (list): A list of coefficients representing a polynomial.
        C (int): A constant.

    Returns:
        tuple: A tuple containing the derivative and integral of the polynomial, 
        including the constant C. If either the polynomial or the constant is invalid, 
        it returns an error message.
    """
    
    # Check if the polynomial is valid (all coefficients are integers and it's not empty)
    if not all(isinstance(x, int) for x in xs) or len(xs) == 0:
        return "Invalid polynomial"
    
    # Check if the constant is an integer
    if not isinstance(C, int):
        return "Invalid constant"
    
    # Calculate the derivative of the polynomial
    derivative = [(i+1)*xs[i+1] for i in range(len(xs)-1)]
    
    # Calculate the integral of the polynomial, including the constant C
    integral = [C] + [xs[i]/(i+1) for i in range(len(xs))]
    
    return derivative, integral