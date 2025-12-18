"""
QUESTION:
Snuke received a triangle as a birthday present. The coordinates of the three vertices were (x_1, y_1), (x_2, y_2), and (x_3, y_3).

He wants to draw two circles with the same radius inside the triangle such that the two circles do not overlap (but they may touch). Compute the maximum possible radius of the circles.

Constraints

* 0 ≤ x_i, y_i ≤ 1000
* The coordinates are integers.
* The three points are not on the same line.

Input

The input is given from Standard Input in the following format:


x_1 y_1
x_2 y_2
x_3 y_3


Output

Print the maximum possible radius of the circles. The absolute error or the relative error must be at most 10^{-9}.

Examples

Input

0 0
1 1
2 0


Output

0.292893218813


Input

3 1
1 5
4 9


Output

0.889055514217
"""

from math import hypot

def calculate_max_circle_radius(x1, y1, x2, y2, x3, y3):
    # Calculate the side lengths of the triangle
    a = hypot(x1 - x2, y1 - y2)
    b = hypot(x2 - x3, y2 - y3)
    c = hypot(x3 - x1, y3 - y1)
    
    # Calculate the area of the triangle using the determinant method
    area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    
    # Calculate the inradius of the triangle
    R = area / (a + b + c)
    
    # Calculate the maximum possible radius of the circles
    m = max(a, b, c)
    r = m / (2 + m / R)
    
    # Return the result with the required precision
    return round(r, 12)