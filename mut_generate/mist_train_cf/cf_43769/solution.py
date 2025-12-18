"""
QUESTION:
Create a function `heron_triangle_area(a, b, c)` that calculates the area of a triangle given its three side lengths `a`, `b`, and `c`. The function must use Heron's formula and include a check to ensure the inputs can form a valid triangle according to the triangle inequality theorem. If the inputs are invalid, the function should return `None`.
"""

def entrance(a, b, c):
    """Compute the area of a triangle using Heron's formula given its three side lengths.
    """
    # Check if inputs can form a valid triangle
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):

        # Compute semi-perimeter
        s = (a + b + c) / 2

        # Compute area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        
        return area

    else:
        # If inputs can't form a valid triangle, return None
        return None