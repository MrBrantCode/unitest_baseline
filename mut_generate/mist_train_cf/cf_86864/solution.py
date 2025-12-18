"""
QUESTION:
Define a function `triangle_type` that takes in three arguments representing the lengths of the sides of a triangle. The function should identify the type of triangle (Equilateral, Isosceles, or Scalene) and perform the following additional calculations:
- If the triangle is Equilateral, calculate and print the area using Heron's formula.
- If the triangle is Isosceles, calculate and print the perimeter.
- If the triangle is Scalene, calculate and print the angles using the Law of Cosines.
The function should also check for invalid input (sides less than or equal to 0, or sides that do not meet the triangle inequality theorem) and print an error message if such conditions are met.
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