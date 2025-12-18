"""
QUESTION:
Write a function named `calculate_area_irregular_pentagon` that takes two parameters: `radius` and `updated_side_length`. This function should calculate and return the area of an irregular pentagon formed by adjusting one side of a regular pentagon inscribed in a circle of the given radius. The adjusted side length is also given. The function should be able to handle different radius sizes and side length changes.
"""

import math

def calculate_area_irregular_pentagon(radius, updated_side_length):
    regular_area = 5/4 * math.tan(math.pi/5) * (2 * radius * math.sin(math.pi / 5))**2
    
    original_side_length = 2 * radius * math.sin(math.pi / 5)
    delta_length = updated_side_length - original_side_length
    
    height_change = delta_length * math.cos(math.pi / 5)
    base_change = delta_length * math.sin(math.pi / 5)
    
    area_change = height_change * base_change
    
    new_area = regular_area + area_change
    return new_area