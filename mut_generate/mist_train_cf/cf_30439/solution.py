"""
QUESTION:
Implement a function `calculate_intersection(xs1, ys1, xe1, ye1, xs2, ys2, xe2, ye2)` that takes the start and end points of two line segments as input and returns the coordinates of the intersection point if it exists, or a specific message indicating if the line segments are parallel or overlapping. The input coordinates are integers and the line segments are not vertical, with a precision threshold defined by a constant `PRECISION`.
"""

PRECISION = 1e-9

def intersection(xs1, ys1, xe1, ye1, xs2, ys2, xe2, ye2):
    # Calculate the slopes and y-intercepts of the two line segments
    m1, b1 = 0.0, 0.0
    m2, b2 = 0.0, 0.0

    if abs(xe1 - xs1) > PRECISION:
        m1 = (ye1 - ys1) / (xe1 - xs1)
        b1 = ys1 - m1 * xs1
    else:
        m1 = 1
        b1 = -xs1

    if abs(xe2 - xs2) > PRECISION:
        m2 = (ye2 - ys2) / (xe2 - xs2)
        b2 = ys2 - m2 * xs2
    else:
        m2 = 1
        b2 = -xs2

    # Check if the line segments are parallel
    if abs(m1 - m2) < PRECISION:
        # Check if the line segments are overlapping
        if abs(b1 - b2) < PRECISION:
            return "Line segments are overlapping"
        else:
            return "Line segments are parallel and non-overlapping"
    else:
        # Calculate the intersection point
        x_intersect = (b2 - b1) / (m1 - m2)
        y_intersect = m1 * x_intersect + b1
        return (x_intersect, y_intersect)