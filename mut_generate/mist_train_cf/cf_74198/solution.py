"""
QUESTION:
Create a function `classify_triangle(a, b, c)` that takes the lengths of three sides of a triangle as input and returns the classification of the triangle as 'Not a triangle', 'Equilateral triangle', 'Isosceles triangle', or 'Scalene triangle'. The classification should be determined using the triangle inequality principle and the equality of the side lengths.
"""

def classify_triangle(a, b, c):
    # Check for triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
    
    # Check for an equilateral triangle
    if a == b and b == c:
        return 'Equilateral triangle'
        
    # Check for an isosceles triangle
    elif a == b or b == c or a == c:
        return 'Isosceles triangle'
    
    # If none of the above checks are true, it must be a scalene triangle
    else:
        return 'Scalene triangle'