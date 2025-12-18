"""
QUESTION:
Write a function `calculate_sum_of_areas` that takes a list of circles as input, where each circle is a dictionary containing 'radius' and 'x' keys. The 'radius' should be a positive integer between 1 and 10, and the 'x' coordinate should be a positive float between 0 and 100. The input list should contain between 1 and 1000 circles. The function should return the sum of the areas of all valid circles, rounded to two decimal places.
"""

import math

def calculate_sum_of_areas(circles):
    total_area = 0
    for circle in circles:
        radius = circle['radius']
        x = circle['x']
        if 1 <= radius <= 10 and 0 <= x <= 100:
            area = math.pi * (radius ** 2)
            total_area += area
    return round(total_area, 2)