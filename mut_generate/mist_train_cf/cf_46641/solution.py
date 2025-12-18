"""
QUESTION:
Create a function called `evaluate_polynomial` that takes in a list of coefficients of a polynomial equation and returns the degree of the polynomial and the leading coefficient. The coefficients should be ordered from the highest power of x to the lowest. Assume that the input list is not empty and that the polynomial is not a constant.
"""

def evaluate_polynomial(coefficients):
    """
    This function takes a list of coefficients of a polynomial equation 
    and returns the degree of the polynomial and the leading coefficient.
    
    Parameters:
    coefficients (list): A list of coefficients of a polynomial equation.
                         The coefficients are ordered from the highest power of x to the lowest.
    
    Returns:
    tuple: A tuple containing the degree of the polynomial and the leading coefficient.
    """
    
    # Remove leading zeros
    while len(coefficients) > 1 and coefficients[0] == 0:
        coefficients.pop(0)
        
    # The degree of the polynomial is determined by the highest power of x
    degree = len(coefficients) - 1
    
    # The leading coefficient is the coefficient of the highest degree term
    leading_coefficient = coefficients[0]
    
    return degree, leading_coefficient