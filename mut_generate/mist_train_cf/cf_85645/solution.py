"""
QUESTION:
Write a function `derivative_and_integral` that takes a list of coefficients representing a polynomial and a constant `C` as input. The function should return the derivative and integral of the polynomial in the same format, incorporating the constant `C`. The function should also validate the input polynomial and constant, returning an error message if either is invalid. The polynomial is valid if it has at least one term and all coefficients are integers. The constant `C` is valid if it is an integer.
"""

def derivative_and_integral(xs: list, C: int):
    """
    xs denotes the coefficients of a given polynomial. xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Function should output the derivative and integral of this polynomial in an identical format, incorporating C.
    It should also return an error if the polynomial or constant C is invalid.
    """
    
    # Check if the polynomial is an empty list
    if len(xs) == 0:
        return "Invalid polynomial"
    
    # Check if the coefficients of the polynomial are integers
    for coeff in xs:
        if not isinstance(coeff, int):
            return "Invalid polynomial"
            
    # Check if constant C is an integer
    if not isinstance(C, int):
        return "Invalid constant"
        
    # Calculate the derivative of the polynomial
    derivative = [i*x for i, x in enumerate(xs)][1:]
    
    # Calculate the integral of the polynomial
    integral = [C] + [x/(i+1) for i, x in enumerate(xs)]
    
    return derivative, integral