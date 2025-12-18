"""
QUESTION:
Write a Python function `linear_approximation` that uses the formula for linear approximation to estimate the value of a function at a given point. The function should take four arguments: `a` (the point at which the value and derivative of the function are known), `F_a` (the value of the function at `a`), `F_prime_a` (the derivative of the function at `a`), and `x` (the point near `a` that we want to estimate the function at). The function should return the estimated value of the function at `x`. Assume that the function `F` is differentiable and that `x` is close to `a`.
"""

def linear_approximation(a, F_a, F_prime_a, x):
    """
    Uses the formula for linear approximation to estimate the value of a function at a given point.

    Args:
        a (float): The point at which the value and derivative of the function are known.
        F_a (float): The value of the function at a.
        F_prime_a (float): The derivative of the function at a.
        x (float): The point near a that we want to estimate the function at.

    Returns:
        float: The estimated value of the function at x.
    """
    return F_a + F_prime_a * (x - a)