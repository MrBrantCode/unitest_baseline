"""
QUESTION:
Create a function called `linear_interpolation_custom` that takes five arguments: `x1`, `y1`, `x2`, `y2`, and `x`, where `(x1, y1)` and `(x2, y2)` are two given points and `x` is the value at which you want to interpolate `y`. The function should use a custom equation instead of the standard formula for linear interpolation. The custom equation is `y = (y1 * (x2 - x) + y2 * (x - x1)) / (x2 - x1)`.
"""

def linear_interpolation_custom(x1, y1, x2, y2, x):
    """
    This function performs linear interpolation using a custom equation.
    
    Args:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.
    x (float): The x-value at which to interpolate y.

    Returns:
    float: The interpolated y-value at the given x.
    """

    # Calculate the interpolated y-value using the custom equation
    y = (y1 * (x2 - x) + y2 * (x - x1)) / (x2 - x1)
    
    return y