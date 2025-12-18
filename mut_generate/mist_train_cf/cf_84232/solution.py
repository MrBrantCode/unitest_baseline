"""
QUESTION:
Write a function named `derivative_and_integral` that calculates the derivative and integral of a given polynomial, represented as a list of coefficients `xs`, with an integration constant `C`. The coefficients in `xs` are ordered from the constant term to the highest degree term. The function should return the coefficients of the derivative and integral polynomials as two lists. The integral should be calculated with the integration constant `C`.
"""

def derivative_and_integral(xs: list, C: int):
    """
    This function calculates the derivative and integral of a given polynomial.

    Args:
        xs (list): A list of coefficients representing the polynomial, ordered from the constant term to the highest degree term.
        C (int): The integration constant.

    Returns:
        tuple: A tuple containing two lists. The first list represents the coefficients of the derivative polynomial,
               and the second list represents the coefficients of the integral polynomial.
    """
    derivative = [i*coeff for i, coeff in enumerate(xs)][1:]
    integral = [C] + [coeff/(i+1) for i, coeff in enumerate(xs)]
    return derivative, integral