"""
QUESTION:
Evaluate a polynomial using Horner's method. Implement a function `horner_evaluation(coefficients, x)` that takes as input a list of coefficients representing a polynomial equation in descending order of powers and a value for `x`, and returns the result of the polynomial evaluation.
"""

def horner_evaluation(coefficients, x):
    """
    Evaluate a polynomial using Horner's method.

    Args:
    coefficients (list): A list of coefficients representing a polynomial equation in descending order of powers.
    x (float): The input value for the polynomial evaluation.

    Returns:
    float: The result of the polynomial evaluation.
    """
    result = 0
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result