"""
QUESTION:
Design a function `heron_triangle_area` to calculate the area of a triangle using Heron's formula, given three side lengths `a`, `b`, and `c` as input. The function should return the calculated area. Note that the input side lengths are expected to form a valid triangle, but the function does not need to check for this condition.
"""

import math

def heron_triangle_area(a, b, c):
    """With the given side lengths, compute the area of the triangle using Heron's formula."""
    # compute the semi-perimeter
    s = (a + b + c) / 2.0

    # compute the area
    return math.sqrt(s * (s - a) * (s - b) * (s - c))