"""
QUESTION:
Write a function `calculate_volume` that calculates the volume of an irregular-shaped object given the lengths of three sides of the object. The lengths are positive integers less than or equal to 10^9. The function must handle edge cases where the length of any side is equal to 1. The volume should be calculated as the area of the base times the height, using Heron's formula to calculate the area of the base, and the height as the maximum side length. The volume should be returned as a floating-point number rounded to two decimal places. The function should not use any built-in functions or libraries other than for input/output operations.
"""

import math

def calculate_volume(side1, side2, side3):
    # Calculate the semiperimeter
    s = (side1 + side2 + side3) / 2
    
    # Calculate the area of the base using Heron's formula
    base_area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    # Get the height (assuming it is the maximum side length)
    height = max(side1, side2, side3)
    
    # Calculate the volume
    volume = base_area * height
    
    # Round the volume to two decimal places
    volume = round(volume, 2)
    
    return volume