"""
QUESTION:
Implement the `derivative_and_integral` function to calculate the derivative and integral of a polynomial with real or complex coefficients, given as a list of coefficients in ascending order of powers. The function should handle decimal coefficients and include a constant of integration `C`, which can also be a complex number. The output should be two lists representing the coefficients of the derivative and integral polynomials, respectively, with no trailing zeros.
"""

def derivative_and_integral(xs: list, C: complex) -> list:
    # Differentiation
    der = [i*xs[i] for i in range(1, len(xs))]

    # Integration
    integral = [C] + [xs[i]/(i+1) for i in range(len(xs))]

    # To remove trailing zeros for both derivative and integral.
    while len(der) > 0 and abs(der[-1]) == 0: 
        der.pop()

    while len(integral) > 0 and abs(integral[-1]) == 0:  
        integral.pop()

    return der, integral