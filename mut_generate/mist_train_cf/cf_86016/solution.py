"""
QUESTION:
Write a function named `calculate_volume` that takes three parameters: `base_type`, `side`, and `height`. The function should calculate the volume of a regular pyramid with the given base type, side length, and height. The base type can be "square", "triangle", or "pentagon". The function should return the calculated volume using the formula `V = (1/3) * base_area * height`, where the base area is calculated according to the base type.
"""

import math

def calculate_volume(base_type, side, height):
    base_area = 0

    if base_type == "square":
        base_area = side ** 2
    elif base_type == "triangle":
        # semi-perimeter of the triangle
        s = 1.5 * side
        base_area = math.sqrt(s * (s - side) ** 3)
    elif base_type == "pentagon":
        base_area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2
    else:
        print("Invalid base type")
        return None
        
    return base_area * height / 3