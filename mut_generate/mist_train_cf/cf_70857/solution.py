"""
QUESTION:
Write a function `derivative_and_integral` that calculates the derivative and integral of a polynomial given its coefficients. The polynomial is represented by a list of coefficients `xs` where the polynomial is `xs[0] + xs[1] * x + xs[2] * x^2 + ...`. The function should return the coefficients of the derivative and integral in the same form, with the integral including a constant of integration `C`. The function should assume that the input list `xs` is not empty and that the constant of integration `C` is an integer.
"""

def derivative_and_integral(xs: list, C: int):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative and integral of this polynomial in the same form, adding C.
    """

    # Calculate the derivative
    derivative = []
    for i in range(1, len(xs)):
        derivative.append(i * xs[i])

    # Calculate the integral
    integral = [C]
    for i in range(len(xs)):
        integral.append(xs[i] / (i + 1))

    return derivative, integral