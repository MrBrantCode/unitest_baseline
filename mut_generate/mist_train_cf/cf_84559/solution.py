"""
QUESTION:
Create a function to calculate the surface area and volume of a triangular prism. The function should take four parameters: the lengths of three sides of the triangular base (a, b, c) and the height of the prism (h). The function should ensure that the inputs are valid (i.e., non-negative and form a valid triangle). The function should be able to handle at most 10,000 inputs efficiently. The function should also handle edge cases of extremely small and large values. The function should return the surface area and volume of the prism. The function can use Heron's formula to calculate the area of the base triangle.
"""

import math

def triangular_prism_properties(a, b, c, h):
    """Return the surface area and volume of a triangular prism."""
    assert a >= 0 and b >= 0 and c >= 0 and h >= 0, "Ensure non-negative prism dimensions"
    assert a + b > c and b + c > a and c + a > b, "Ensure valid triangle dimensions"

    # Calculate semi-perimeter
    s = (a + b + c) / 2

    # Calculate base area using Heron's formula
    base_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Calculate surface area
    surface_area = (a * h) + (b * h) + (c * h) + 2 * base_area

    # Calculate volume
    volume = base_area * h

    return surface_area, volume