"""
QUESTION:
Define a function called `triangle_type` that takes in three arguments for the lengths of the sides of a triangle and identifies the type of triangle formed by the given sides. The function should check for errors and calculate additional information based on the type of triangle.

The function must follow these rules and restrictions: 

- It should check if any of the sides are equal to zero or negative, and if so, print an error message and return.
- It should check if the sum of any two sides is less than or equal to the third side, and if so, print an error message and return.
- If the triangle is equilateral, it should calculate and print the area of the triangle using Heron's formula.
- If the triangle is isosceles, it should calculate and print the perimeter of the triangle.
- If the triangle is scalene, it should calculate and print the angles of the triangle using the Law of Cosines.
"""

import math

def triangle_type(side1, side2, side3):
    # Check if any side is zero or negative
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Error: Sides must be positive numbers")
        return
    
    # Check triangle inequality theorem
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        print("Error: Invalid triangle")
        return
    
    # Check if all sides are equal
    if side1 == side2 == side3:
        print("Equilateral triangle")
        
        # Calculate area using Heron's formula
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        print("Area:", area)
        
        return
    
    # Check if exactly two sides are equal
    if side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles triangle")
        
        # Calculate perimeter
        perimeter = side1 + side2 + side3
        print("Perimeter:", perimeter)
        
        return
    
    # Calculate angles using Law of Cosines
    angle1 = math.degrees(math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3)))
    angle2 = math.degrees(math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3)))
    angle3 = 180 - angle1 - angle2
    
    print("Scalene triangle")
    print("Angles:", [angle1, angle2, angle3])