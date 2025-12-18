"""
QUESTION:
Create a function `calculate_triangle_perimeter` that takes three integer parameters `a`, `b`, and `c` representing the side lengths of a triangle. The function should return the perimeter of the triangle if the side lengths are valid (all greater than 0 and the sum of any two sides is greater than the third side) and -1 otherwise.
"""

def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return -1