"""
QUESTION:
Write a function `find_quadrant(x, y)` that takes the x and y coordinates of a point as input and returns the quadrant in the Cartesian coordinate system where the point lies. The function should return "First Quadrant", "Second Quadrant", "Third Quadrant", or "Fourth Quadrant" depending on the coordinates. If the point is at the origin (0, 0), the function should return "Origin".
"""

def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "First Quadrant"
    elif x < 0 and y > 0:
        return "Second Quadrant"
    elif x < 0 and y < 0:
        return "Third Quadrant"
    elif x > 0 and y < 0:
        return "Fourth Quadrant"
    else:
        return "Origin"