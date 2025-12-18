"""
QUESTION:
Create a program with the following functions: `is_right_triangle(a, b, c)`, `is_equilateral_triangle(a, b, c)`, `is_isosceles_triangle(a, b, c)`, `calculate_area(a)`, `calculate_perimeter(a, b, c)`, `calculate_angles(a, b, c)`. 

The function `is_right_triangle(a, b, c)` should return `True` if the sides `a`, `b`, `c` form a right-angled triangle and `False` otherwise. The function `is_equilateral_triangle(a, b, c)` should return `True` if the sides `a`, `b`, `c` form an equilateral triangle and `False` otherwise. The function `is_isosceles_triangle(a, b, c)` should return `True` if the sides `a`, `b`, `c` form an isosceles triangle and `False` otherwise. The function `calculate_area(a)` should return the area of an equilateral triangle with side `a`. The function `calculate_perimeter(a, b, c)` should return the perimeter of the triangle with sides `a`, `b`, `c`. The function `calculate_angles(a, b, c)` should return the angles of the triangle with sides `a`, `b`, `c`. 

The program should check the type of the triangle and calculate and display the required values based on the type of the triangle. The program should take the lengths of the sides of the triangle as input from the user and should handle the calculations with floating point precision.
"""

import math

def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    else:
        return False

def is_equilateral_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False

def is_isosceles_triangle(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False

def calculate_area(a):
    area = (math.sqrt(3) / 4) * a**2
    return area

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def calculate_angles(a, b, c):
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return angle_a, angle_b, angle_c