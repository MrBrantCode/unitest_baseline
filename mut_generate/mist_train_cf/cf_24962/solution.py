"""
QUESTION:
Write a function `trapezoidal_rule` that approximates the definite integral of a given function using the trapezoidal rule. The function should take as input the function to integrate, the lower and upper bounds of the integral, and the number of subintervals to divide the area into.
"""

def trapezoidal_rule(f, lower_bound, upper_bound, num_subintervals):
    """
    Approximates the definite integral of a given function using the trapezoidal rule.

    Args:
        f (function): The function to integrate.
        lower_bound (float): The lower bound of the integral.
        upper_bound (float): The upper bound of the integral.
        num_subintervals (int): The number of subintervals to divide the area into.

    Returns:
        float: The approximate value of the definite integral.
    """

    # Calculate the width of each subinterval
    h = (upper_bound - lower_bound) / num_subintervals

    # Calculate the sum of the function values at the subinterval points
    integral = (f(lower_bound) + f(upper_bound)) / 2
    for i in range(1, num_subintervals):
        integral += f(lower_bound + i * h)

    # Calculate the approximate integral using the trapezoidal rule
    integral *= h

    return integral