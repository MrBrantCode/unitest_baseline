"""
QUESTION:
Write a function called `evaluate_polynomial` that takes in a list of coefficients representing a polynomial, and an input value x, and returns the value of the polynomial at x. The coefficients are in descending order of powers.
"""

def evaluate_polynomial(coefficients, x):
    """
    Evaluate the polynomial at x.

    Args:
    coefficients (list): A list of coefficients representing a polynomial, 
                         in descending order of powers.
    x (float): The input value.

    Returns:
    float: The value of the polynomial at x.
    """
    result = 0
    for power, coefficient in enumerate(coefficients):
        result += coefficient * (x ** (len(coefficients) - 1 - power))
    return result