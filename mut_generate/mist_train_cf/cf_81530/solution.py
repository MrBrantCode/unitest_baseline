"""
QUESTION:
Write a function named `calculate_computational_cost` to estimate the computational cost of a single Gauss-Newton method update given the Jacobian matrix J of an objective function. Assume the Jacobian matrix has already been calculated. The cost should be expressed in terms of the number of variables 'n'.
"""

def calculate_computational_cost(n):
    """
    Estimate the computational cost of a single Gauss-Newton method update.

    Args:
        n (int): The number of variables.

    Returns:
        int: The estimated computational cost.
    """
    return n**3