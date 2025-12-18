"""
QUESTION:
Write a Python function named `is_differentiable` that checks if a given activation function is differentiable at a specific point. The function should take as input the activation function, its derivative function, and a point to check. If the derivative function is undefined at the point, the function should return False; otherwise, it should return True. Assume that the derivative function will handle the case where the derivative is undefined by raising a ValueError.
"""

def is_differentiable(activation_function, derivative_function, point):
    """
    Checks if a given activation function is differentiable at a specific point.

    Args:
        activation_function (function): The activation function to check.
        derivative_function (function): The derivative of the activation function.
        point (float): The point to check.

    Returns:
        bool: True if the derivative function is defined at the point, False otherwise.
    """
    try:
        derivative_function(point)
        return True
    except ValueError:
        return False