"""
QUESTION:
Create a function named `assign_variables` that takes an integer `n` as input and assigns values to `n` variables in a pattern where each variable is assigned a value equal to its position (starting from 1). The function should return the assigned values.
"""

def assign_variables(n):
    """
    Assigns values to n variables in a pattern where each variable is assigned a value equal to its position (starting from 1).

    Args:
        n (int): The number of variables.

    Returns:
        list: A list of assigned values.
    """
    return list(range(1, n + 1))