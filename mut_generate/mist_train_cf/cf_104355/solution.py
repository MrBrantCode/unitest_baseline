"""
QUESTION:
Write a recursive function `evaluatePolynomial(coefficients, degree, x)` to evaluate a polynomial of degree `degree` at a given value `x`. The function should take an array of coefficients, the degree of the polynomial, and the value of x as input, where the coefficients are ordered by increasing powers of x. The function should return the value of the polynomial at x.
"""

def evaluatePolynomial(coefficients, degree, x):
    """
    Evaluate a polynomial of degree 'degree' at a given value 'x'.

    Args:
        coefficients (list): Array of coefficients, ordered by increasing powers of x.
        degree (int): Degree of the polynomial.
        x (float): Value at which to evaluate the polynomial.

    Returns:
        float: Value of the polynomial at x.
    """
    if degree == 0:
        return coefficients[0]
    else:
        return coefficients[degree] * x**degree + evaluatePolynomial(coefficients, degree - 1, x)