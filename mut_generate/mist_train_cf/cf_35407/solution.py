"""
QUESTION:
Implement a function `rotate_dataset(dataset, angle)` that takes in a list of 2D points `dataset` and a rotation angle `angle` in degrees, and returns a new list of points rotated by the specified angle in a counterclockwise direction around the origin (0, 0). The input `dataset` is a list of tuples, where each tuple contains the x and y coordinates of a point. The input `angle` can be any real number.
"""

import math

def rotate_dataset(dataset, angle):
    angle_rad = math.radians(angle)
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)
    return [(x * cos_angle - y * sin_angle, x * sin_angle + y * cos_angle) for x, y in dataset]