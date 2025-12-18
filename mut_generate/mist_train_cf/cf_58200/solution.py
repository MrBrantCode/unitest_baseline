"""
QUESTION:
Write a function called `calculate_slope` that takes the coordinates of two points (x1, y1) and (x2, y2) as input and returns the slope of the line passing through these two points using the formula m = (y2 - y1) / (x2 - x1). The function should not take any other parameters and should return the slope value as a number.
"""

def calculate_slope(x1, y1, x2, y2):
    """
    Calculate the slope of the line passing through two points.

    Parameters:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.

    Returns:
    float: The slope of the line passing through the two points.
    """
    return (y2 - y1) / (x2 - x1)