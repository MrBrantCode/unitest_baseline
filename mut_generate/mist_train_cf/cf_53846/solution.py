"""
QUESTION:
Write a function `is_on_curve` that checks whether a point (x, y) lies on an elliptic curve defined by the equation y^2 = x^3 + ax + b. The function should take four parameters: x and y coordinates of the point, and coefficients a and b of the elliptic curve.
"""

def is_on_curve(x, y, a, b):
    """
    Checks whether a point (x, y) lies on an elliptic curve defined by the equation y^2 = x^3 + ax + b.

    Args:
        x (int): x-coordinate of the point
        y (int): y-coordinate of the point
        a (int): coefficient a of the elliptic curve
        b (int): coefficient b of the elliptic curve

    Returns:
        bool: True if the point lies on the curve, False otherwise
    """
    return y**2 == x**3 + a*x + b