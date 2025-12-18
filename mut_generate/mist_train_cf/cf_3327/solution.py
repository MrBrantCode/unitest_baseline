"""
QUESTION:
Implement a CentroidCalculator class with a function calculate_centroid that takes a list of Point objects as input. The function should return the centroid as a tuple rounded to the nearest integer if all the following conditions are met: 
- The number of points is less than or equal to 10.
- All points have distinct x-coordinates.
- All points have positive y-coordinates.
- All points have even x-coordinates.
If the conditions are not met, the function should return None.
"""

def calculate_centroid(points):
    """
    Calculate the centroid of a list of points.

    Args:
    points (list): A list of Point objects.

    Returns:
    tuple: The centroid as a tuple rounded to the nearest integer if all conditions are met, otherwise None.
    """
    
    # Check if the number of points is less than or equal to 10
    if len(points) > 10:
        return None

    # Check if all points have distinct x-coordinates
    if len(set(point.x for point in points)) != len(points):
        return None

    # Check if all points have positive y-coordinates and even x-coordinates
    for point in points:
        if point.y <= 0 or point.x % 2 != 0:
            return None
    
    # Calculate the centroid
    sum_x = sum(point.x for point in points)
    sum_y = sum(point.y for point in points)
    count = len(points)
    
    centroid_x = sum_x / count
    centroid_y = sum_y / count
    
    return (round(centroid_x), round(centroid_y))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y