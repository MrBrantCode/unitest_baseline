"""
QUESTION:
Create a function named `determine_triangle_type` that takes three arguments representing the side lengths of a triangle. The function should first check if the triangle is valid, meaning the sum of any two sides must be greater than the third side. If the triangle is valid, the function should then determine its type based on the following conditions: 
- Equilateral: all three sides are equal.
- Isosceles and right-angled: two sides are equal and the triangle is a right triangle.
- Isosceles: two sides are equal and the triangle is not a right triangle.
- Scalene and right-angled: all three sides are different and the triangle is a right triangle.
- Scalene: all three sides are different and the triangle is not a right triangle.
If the triangle is not valid, the function should return an error message.
"""

def determine_triangle_type(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Error: Invalid triangle"
    elif side1 == side2 == side3:
        return "Equilateral triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
            return "Isosceles and right-angled triangle"
        else:
            return "Isosceles triangle"
    else:
        if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
            return "Scalene and right-angled triangle"
        else:
            return "Scalene triangle"