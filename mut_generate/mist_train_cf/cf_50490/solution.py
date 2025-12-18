"""
QUESTION:
Write a function `calculate_heights` that takes an array of tuples, where each tuple contains a base and an angle, and returns an array of heights of right-angled triangles. The function should use the trigonometric principle and account for edge cases where the input values might lead to non-triangle or non-real triangles. The angle is measured in degrees and is the angle of the non-right angled vertex. The function should return 'Invalid triangle' for invalid angles (less than or equal to 0 or greater than or equal to 90 degrees).
"""

import math

def calculate_heights(triangle_array):
    heights = []
    for base, angle in triangle_array:
        if angle <= 0 or angle >= 90:
            heights.append('Invalid triangle')
        else:
            radian = math.radians(angle)
            height = base * math.sin(radian)
            heights.append(height)
    return heights