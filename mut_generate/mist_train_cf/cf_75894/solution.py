"""
QUESTION:
Develop a function called `find_roots(a, b, c, d)` that calculates a real root of a cubic equation ax³ + bx² + cx + d = 0 using Newton's method, where a, b, c, and d are coefficients of the cubic equation. The function should return one real root of the equation with a precision of at least 1e-6, regardless of the initial guess.
"""

def find_roots(a, b, c, d):
    """
    Calculate a real root of a cubic equation ax³ + bx² + cx + d = 0 using Newton's method.

    Args:
        a (float): Coefficient of x³ term.
        b (float): Coefficient of x² term.
        c (float): Coefficient of x term.
        d (float): Constant term.

    Returns:
        float: A real root of the cubic equation with a precision of at least 1e-6.
    """
    f = lambda x: a*x**3 + b*x**2 + c*x + d
    df = lambda x: 3*a*x**2 + 2*b*x + c
    x = 0
    while abs(f(x)) > 1e-6:
        x = x - f(x)/df(x)
    return x