"""
QUESTION:
Create a function called `triangle_area` that calculates the area of an isosceles triangle given the lengths of its two equal sides (Side1 and Side2) and the base. The function should handle invalid inputs such as negative side lengths, unequal side lengths, and combinations of side lengths that cannot form a valid triangle.
"""

import math

def triangle_area(s1, s2, base):
    """Calculate the area of the isosceles triangle"""
    if s1 == s2 and ((s1 + s2) > base) and all(i > 0 for i in (s1, s2, base)):
        s = (s1 + s2 + base) / 2  # Semi-perimeter
        area = math.sqrt(s * (s - s1) * (s - s2) * (s - base))  # Heron's Formula
        return area
    else:
        return "Invalid inputs, unable to form a valid isosceles triangle"