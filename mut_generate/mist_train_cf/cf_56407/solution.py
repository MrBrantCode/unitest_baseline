"""
QUESTION:
Write a function `check_probability_range` that takes a discrete random variable `y` and its function `q(y)` as input. The function should return `True` if the value of `q(y)` lies within the range [0, 1] for every unique value of `y`, and `False` otherwise.
"""

def check_probability_range(y, q):
    """
    This function checks if the value of q(y) lies within the range [0, 1] 
    for every unique value of y.

    Args:
        y (list): A discrete random variable.
        q (function): A function that takes y as input.

    Returns:
        bool: True if q(y) lies within [0, 1] for every unique value of y, False otherwise.
    """
    # Get unique values of y
    unique_y = set(y)
    
    # Check if q(y) lies within [0, 1] for every unique value of y
    for value in unique_y:
        if not 0 <= q(value) <= 1:
            return False
    
    return True