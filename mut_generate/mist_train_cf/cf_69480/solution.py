"""
QUESTION:
Write a function `derivative` that takes a vector of coefficients representing a complex exponential series as input and returns the derivative of the series. The input vector's nth element represents the coefficient of the exponential term e^(nx). The function should return a vector where each element is the derivative of the corresponding term in the input series, calculated as (n * coefficient) for the nth term. The input vector will contain at least one element.
"""

def derivative(coefficients):
    """
    This function calculates the derivative of a complex exponential series.
    
    Parameters:
    coefficients (list): A list of coefficients representing a complex exponential series.
    
    Returns:
    list: A list where each element is the derivative of the corresponding term in the input series.
    """
    return [coeff * (i + 1) for i, coeff in enumerate(coefficients)]