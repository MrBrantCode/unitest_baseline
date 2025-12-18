"""
QUESTION:
Calculate the derivative and integral of a polynomial represented by its coefficients. The function `derivative_and_integral` should take a list of coefficients `xs` and a constant of integration `C` as input, and return a tuple containing the coefficients of the derivative and integral polynomials. The coefficients of the input polynomial are ordered from the lowest to the highest power of the variable, i.e., `xs[0]` is the constant term, `xs[1]` is the coefficient of the linear term, and so on. The constant of integration `C` should be included in the integral polynomial. The function should handle edge cases, including empty input lists and polynomials with zero coefficients, and remove any trailing zeros from the output coefficients.
"""

def calculate_derivative_and_integral(xs: list, C: int):
    """
    xs = coefficients of a polynomial (xs[0] + xs[1] * x + xs[2] * x^2 + ....)
    This function returns the derivative and integral of the given polynomial, includes the constant C, and removes trailing zeros.
    """
    derivative = []
    integral = [C]

    for i in range(len(xs)):
        if i != 0:
            derivative.append(i * xs[i])
        if i+1 != 0:
            integral.append(xs[i] / (i+1))

    # Remove trailing zeros
    while integral[-1] == 0:
        integral = integral[:-1] 
    while derivative and derivative[-1] == 0:
        derivative = derivative[:-1]
  
    return derivative, integral