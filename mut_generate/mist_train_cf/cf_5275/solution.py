"""
QUESTION:
Write a function `mean_value` that calculates the mean value of a function defined on a closed interval [a, b], given that the function is continuously differentiable and satisfies certain conditions at the endpoints, and there exists a local minimum or maximum within the interval. The function should only consider the values of the function at the local minimum or maximum point.
"""

def mean_value(f, a, b, c):
    """
    Calculate the mean value of a function defined on a closed interval [a, b], 
    given that the function is continuously differentiable and satisfies certain 
    conditions at the endpoints, and there exists a local minimum or maximum within 
    the interval.

    Parameters:
    f (function): The input function.
    a (float): The start of the interval.
    b (float): The end of the interval.
    c (float): The local minimum or maximum point within the interval.

    Returns:
    float: The mean value of the function.
    """
    return f(c)