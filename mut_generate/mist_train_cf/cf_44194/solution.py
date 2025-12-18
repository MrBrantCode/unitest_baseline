"""
QUESTION:
Write a function named `triangle_properties` that takes three integers `a`, `b`, and `c` representing the side lengths of a triangle as input. The function should calculate the perimeter and area of the triangle using Heron's formula, and classify the triangle based on its side lengths and angles. The classification should be one of the following: 'equilateral', 'isosceles', 'scalene', 'acute-angled', 'right-angled', or 'obtuse-angled'. The function should return a tuple containing the perimeter, area, and classification of the triangle. The input sides are assumed to be non-negative integers, and the function should assert if the provided sides do not form a valid triangle according to the triangle inequality theorem.
"""

import math

def triangle_properties(a, b, c):
    """
    Calculate the perimeter, area, and classification of a triangle given its side lengths.

    Args:
        a (int): The length of the first side.
        b (int): The length of the second side.
        c (int): The length of the third side.

    Returns:
        tuple: A tuple containing the perimeter, area, and classification of the triangle.
    """

    # Check if the sides can form a triangle
    assert a + b > c and a + c > b and b + c > a, "These sides do not form a triangle"

    # Calculate the perimeter
    perimeter = a + b + c 

    # Calculate the semi-perimeter
    s = perimeter / 2 

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 

    # Classifying the triangle based on its side lengths
    if a == b == c:
        shape = 'equilateral'
    elif a == b or a == c or b == c:
        shape = 'isosceles'
    else:
        shape = 'scalene'

    # Classifying the triangle based on its angles
    sides = sorted([a, b, c]) 
    if sides[2]**2 > sides[0]**2 + sides[1]**2:
        angle = 'obtuse-angled'
    elif sides[2]**2 == sides[0]**2 + sides[1]**2:
        angle = 'right-angled'
    else:
        angle = 'acute-angled'

    return (perimeter, area, f'{shape}, {angle}')