"""
QUESTION:
Write a function `grad_to_deg` that takes an angle in gradians as input and returns the equivalent angle in degrees. Assume 1 gradian is equal to 0.9 degrees.
"""

def grad_to_deg(grad):
    """
    Converts an angle in gradians to degrees.

    Args:
        grad (float): The angle in gradians.

    Returns:
        float: The equivalent angle in degrees.
    """
    return grad * 0.9