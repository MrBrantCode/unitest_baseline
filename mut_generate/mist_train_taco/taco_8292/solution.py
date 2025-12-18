"""
QUESTION:
You are given two rectangles on a plane. The centers of both rectangles are located in the origin of coordinates (meaning the center of the rectangle's symmetry). The first rectangle's sides are parallel to the coordinate axes: the length of the side that is parallel to the Ox axis, equals w, the length of the side that is parallel to the Oy axis, equals h. The second rectangle can be obtained by rotating the first rectangle relative to the origin of coordinates by angle α. [Image] 

Your task is to find the area of the region which belongs to both given rectangles. This region is shaded in the picture.


-----Input-----

The first line contains three integers w, h, α (1 ≤ w, h ≤ 10^6; 0 ≤ α ≤ 180). Angle α is given in degrees.


-----Output-----

In a single line print a real number — the area of the region which belongs to both given rectangles.

The answer will be considered correct if its relative or absolute error doesn't exceed 10^{ - 6}.


-----Examples-----
Input
1 1 45

Output
0.828427125

Input
6 4 30

Output
19.668384925



-----Note-----

The second sample has been drawn on the picture above.
"""

from math import sin, cos, tan, atan, pi

def calculate_intersecting_area(w: int, h: int, alpha: int) -> float:
    """
    Calculate the area of the region which belongs to both given rectangles.

    Parameters:
    w (int): The length of the side of the first rectangle parallel to the Ox axis.
    h (int): The length of the side of the first rectangle parallel to the Oy axis.
    alpha (int): The angle of rotation in degrees (0 ≤ alpha ≤ 180).

    Returns:
    float: The area of the intersecting region with a precision of 9 decimal places.
    """
    alpha = min(alpha, 180 - alpha) * pi / 180
    if h > w:
        (h, w) = (w, h)
    if h * (1 + cos(alpha)) < w * sin(alpha):
        res = h * h / sin(alpha)
    else:
        res = h * w - ((w - h * tan(alpha / 2)) ** 2 * tan(alpha) + (h - w * tan(alpha / 2)) ** 2 * tan(alpha)) / 4
    return round(res, 9)