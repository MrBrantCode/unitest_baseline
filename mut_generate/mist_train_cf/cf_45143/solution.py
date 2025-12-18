"""
QUESTION:
Develop a function `calculate_segment_volume` that takes in the radius and central angle of a sphere as input and returns the volume of the segment. The central angle should be in degrees, and the function should convert it to radians internally for calculation. Use the formula V = (π*d^3*θ)/(12*180) where d is the diameter of the sphere.
"""

import math

def calculate_segment_volume(radius, central_angle):
    diameter = 2 * radius
    central_angle_rad = math.radians(central_angle)
    volume_segment = (math.pi * diameter**3 * central_angle_rad) / (12 * 180)
    return volume_segment