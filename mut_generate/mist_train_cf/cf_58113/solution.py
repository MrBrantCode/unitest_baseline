"""
QUESTION:
Write a function `compute_derivative_integral(xs, C)` where `xs` is a list of coefficients representing a polynomial in ascending order of powers, and `C` is the integration constant. The function should calculate both the derivative and integral of the given polynomial, incorporating the constant `C` and removing any trailing zeros. If the input list `xs` is empty, return an empty list for the derivative and a list containing only the constant `C` for the integral.
"""

def compute_derivative_integral(xs: list, C: int):
    """
    Compute both the derivative and integral of the given polynomial, 
    incorporate constant C and remove any surplus zeros.
    """
    if not xs:
        return [], [C]
    
    derivative = []
    integral = [C]

    for i in range(len(xs)):
        if i > 0:  derivative.append(i * xs[i])
        if i > 0:  integral.append(xs[i-1] /(i))
        
    integral.append(xs[-1] / len(xs))

    while derivative and derivative[-1] == 0:
        derivative.pop()
        
    while len(integral) > 1 and integral[-1] == 0:  # retain the constant term even if it's zero.
        integral.pop()

    return derivative, integral