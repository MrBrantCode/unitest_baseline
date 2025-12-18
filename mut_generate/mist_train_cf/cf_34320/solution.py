"""
QUESTION:
Create a function `relative_position(reference_point, other_points)` that determines the relative position of a given point with respect to a set of other points on a 2D plane. The function should take in the coordinates of the reference point as a tuple `(x, y)` and a list of other points, where each point is a tuple `(x, y)`. Return a list of strings indicating whether each point is to the left, right, or on the same vertical line as the reference point.
"""

def relative_position(reference_point, other_points):
    result = []
    x_ref, y_ref = reference_point
    for point in other_points:
        x, y = point
        if x < x_ref:
            result.append('left')
        elif x > x_ref:
            result.append('right')
        else:
            result.append('same line')
    return result