"""
QUESTION:
Write a function `calculate_slope` that takes a list of points as input, where each point is a tuple of two numbers (x, y), and returns the slope of the line formed by these points. Assume that the input list contains at least two distinct points and that the line is not vertical.
"""

def calculate_slope(points):
    """
    Calculate the slope of a line formed by a list of points.

    Args:
        points (list): A list of points, where each point is a tuple of two numbers (x, y).

    Returns:
        float: The slope of the line formed by the points.
    """
    # Choose the first and last points from the list
    x1, y1 = points[0]
    x2, y2 = points[-1]
    
    # Calculate the slope using the formula
    slope = (y2 - y1) / (x2 - x1)
    
    return slope