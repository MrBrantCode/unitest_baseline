"""
QUESTION:
Given a Hessian matrix H of size n x n, determine the computational cost of a single Newton's method update. Assume the Hessian matrix has been pre-computed and is available. Exclude any costs associated with computing the Hessian matrix itself.
"""

def newton_method_cost(n):
    """
    Calculate the computational cost of a single Newton's method update.

    The cost is primarily dictated by the cost of inverting the Hessian matrix, 
    which is O(n^3) for n parameters.

    Args:
        n (int): The number of parameters.

    Returns:
        str: The computational cost in Big O notation.
    """
    return "O(n^3)"