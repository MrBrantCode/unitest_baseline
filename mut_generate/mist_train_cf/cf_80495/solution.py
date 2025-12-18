"""
QUESTION:
Given a sorted array of one-dimensional points with either red or blue color, write a function `find_closest_pair` that finds the closest pair of points with different colors in O(n) time complexity. The input array contains integers representing the points and the color information can be represented as a separate array of colors (0 for red and 1 for blue) or as a single array of tuples containing the point and its color. The output should be the minimum distance between a pair of points with different colors.
"""

def find_closest_pair(points, colors):
    """
    Find the closest pair of points with different colors in O(n) time complexity.

    Args:
        points (list): A sorted list of one-dimensional points.
        colors (list): A list of colors corresponding to the points (0 for red and 1 for blue).

    Returns:
        int: The minimum distance between a pair of points with different colors.
    """
    min_distance = float('inf')
    last_red, last_blue = None, None

    for i, (point, color) in enumerate(zip(points, colors)):
        if color == 0:
            if last_blue is not None:
                min_distance = min(min_distance, abs(point - points[last_blue]))
            last_red = i
        else:
            if last_red is not None:
                min_distance = min(min_distance, abs(point - points[last_red]))
            last_blue = i

    return min_distance