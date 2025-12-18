"""
QUESTION:
Write a function `is_point_outside(points)` that takes a list of points as input where each point is a tuple of two integers (x, y). The function should return the first point that does not satisfy both inequalities y > 9x - 8 and y < -x + 8. If all points satisfy both inequalities, the function should return None.
"""

def entrance(points):
    for point in points:
        x, y = point
        if not(y > 9*x - 8 and y < -x + 8):
            return point
    return None