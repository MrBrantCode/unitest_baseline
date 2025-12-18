"""
QUESTION:
For given two sides of a triangle a and b and the angle C between them, calculate the following properties:

* S: Area of the triangle
* L: The length of the circumference of the triangle
* h: The height of the triangle with side a as a bottom edge



Input

The length of a, the length of b and the angle C are given in integers.

Output

Print S, L and h in a line respectively. The output should not contain an absolute error greater than 10-4.

Example

Input

4 3 90


Output

6.00000000
12.00000000
3.00000000
"""

import math

def calculate_triangle_properties(a: float, b: float, C: float) -> (float, float, float):
    # Convert angle C from degrees to radians
    C_rad = math.radians(C)
    
    # Calculate the area of the triangle (S)
    S = 0.5 * a * b * math.sin(C_rad)
    
    # Calculate the square of the length of the third side (c)
    c2 = a**2 + b**2 - 2 * a * b * math.cos(C_rad)
    
    # Calculate the length of the circumference (L)
    L = a + b + math.sqrt(c2)
    
    # Calculate the height (h) with side a as the bottom edge
    h = 2 * S / a
    
    return S, L, h