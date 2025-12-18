"""
QUESTION:
Write a function `largest_inscribed_triangle` that takes in a radius and optional parameters `h`, `k`, `a`, and `b` to find the area of the largest triangle that can be inscribed in a semicircle or a semicircle of an ellipse shape. The semicircle or ellipse is centered at the point `(h, k)` with a radius or lengths of the major and minor axes `a` and `b`. The function should return the area of the triangle and the coordinates of its vertices. 

The function should handle cases where the semicircle is centered at the origin or a different point, and where the semicircle is a standard semicircle or an elliptical semicircle. It should also handle invalid inputs and return an error message in such cases. The radius and lengths of the axes must be positive numbers.
"""

from math import sqrt

def largest_inscribed_triangle(radius, h=0, k=0, a=None, b=None):
    if (not isinstance(radius, (int, float))) or (radius <= 0):
        return "Error: Radius must be a positive number."
    if (not isinstance(h, (int, float))) or (not isinstance(k, (int, float))):
        return "Error: Center coordinates must be numbers."
    if a is not None and b is not None:
        if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
            return "Error: Major and minor axes must be numbers."
        if a <= 0 or b <= 0:
            return "Error: Lengths of axes must be positive numbers."
        area = 0.5 * a * b / sqrt(2) * b / sqrt(2)
        vertices = [(h,h), (k-a/sqrt(2), k-b/sqrt(2)), (k+a/sqrt(2), k+b/sqrt(2))]
    else:
        area = 0.5 * radius * radius
        vertices = [(h-radius, k), (h+radius, k), (h, k+radius)]
    return area, vertices