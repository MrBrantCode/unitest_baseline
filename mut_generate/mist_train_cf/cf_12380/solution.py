"""
QUESTION:
Implement a function named `simpsons_rule(f, a, b, n)` that approximates the definite integral of a given function `f` from `a` to `b` using Simpson's rule with `n` intervals. The function `f` is an input representing the function to be integrated, and it should be called within `simpsons_rule` to evaluate the function at different points.
"""

def simpsons_rule(f, a, b, n):
    """
    Approximates the definite integral of a given function f from a to b using Simpson's rule with n intervals.

    Args:
        f (function): The function to be integrated.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of intervals.

    Returns:
        float: The approximate value of the integral.
    """

    # Calculate the width of each interval
    h = (b - a) / n
    
    # Initialize the integral with the function values at the endpoints
    integral = f(a) + f(b)

    # Iterate over the intervals
    for i in range(1, n):
        # Calculate the x-coordinate of the current point
        x = a + i * h
        
        # Apply Simpson's rule coefficients
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    # Multiply by the width of the intervals and divide by 3
    integral *= h / 3
    
    return integral