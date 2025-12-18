"""
QUESTION:
Write a function named `triangle_type` that determines the type of triangle characterized by three side lengths a, b, and c. The function should return 'Equilateral' if all sides are equal, 'Isosceles' if only two sides are equal, 'Scalene' if all sides are unequal, and 'Not a triangle' if the lengths cannot form a triangle.
"""

def triangle_type(a, b, c):
    # Check triangle inequality theorem
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    
    # Check for equilateral triangle
    elif a == b == c:
        return "Equilateral"
    
    # Check for isosceles triangle
    elif a == b or a == c or b == c:
        return "Isosceles"
    
    # Else it is a scalene triangle
    else:
        return "Scalene"