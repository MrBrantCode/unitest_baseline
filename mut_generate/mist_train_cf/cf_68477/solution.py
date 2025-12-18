"""
QUESTION:
Write a function `min_bounding_box` that calculates the smallest rectangle that completely contains a given convex polygon. The input is a list of 2D points that define the vertices of the convex polygon. The function should return the minimum and maximum x and y coordinates of the rectangle.
"""

def min_bounding_box(points):
    """
    Calculate the smallest rectangle that completely contains a given convex polygon.

    Args:
    points (list): A list of 2D points that define the vertices of the convex polygon.

    Returns:
    tuple: A tuple of four values representing the minimum and maximum x and y coordinates of the rectangle.
    """
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    return min_x, min_y, max_x, max_y