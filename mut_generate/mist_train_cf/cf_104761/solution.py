"""
QUESTION:
Create a function `linear_interpolation` that performs linear interpolation between two points using polynomial regression. The function should take in the coordinates of two points `(x1, y1)` and `(x2, y2)`, and a value `x` for which to find the corresponding `y` value. The function should return the interpolated `y` value.
"""

def linear_interpolation(x1, y1, x2, y2, x):
    """
    Performs linear interpolation between two points using polynomial regression.
    
    Args:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.
    x (float): The value for which to find the corresponding y value.
    
    Returns:
    float: The interpolated y value.
    """
    # Calculate the slope (m) of the linear regression line
    m = (y2 - y1) / (x2 - x1)
    
    # Calculate the y-intercept (b) of the linear regression line
    b = y1 - m * x1
    
    # Interpolate the y value using the equation y = mx + b
    return m * x + b