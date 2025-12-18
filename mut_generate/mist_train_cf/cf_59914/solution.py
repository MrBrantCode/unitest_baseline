"""
QUESTION:
Implement a function `taylor_series_approximation` to calculate the Taylor series approximation of `sin(5x) / x` around `x=0` without using any symbolic computation library. The function should take two arguments: `x` and `degree`, where `x` is the input value and `degree` is the degree of the Taylor series approximation. The function should return the approximated value and the error in the approximation. Assume that `x` is in the domain (-1, 1).
"""

def taylor_series_approximation(x, degree):
    """
    Calculate the Taylor series approximation of sin(5x) / x around x=0.

    Args:
    x (float): The input value.
    degree (int): The degree of the Taylor series approximation.

    Returns:
    tuple: A tuple containing the approximated value and the error in the approximation.
    """
    
    # Initialize the sum of the Taylor series
    taylor_sum = 5
    
    # Calculate the Taylor series up to the given degree
    for n in range(1, degree + 1):
        # Calculate the sign of the term
        sign = (-1) ** n
        
        # Calculate the term
        term = ((5 * x) ** (2 * n)) / (math.factorial(2 * n + 1))
        
        # Add the term to the sum
        taylor_sum += sign * term
    
    # Calculate the error in the approximation
    error = abs((-1) ** (degree + 1) * (5 ** (2 * degree + 1)) / math.factorial(2 * degree + 1))
    
    return taylor_sum, error