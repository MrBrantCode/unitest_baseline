"""
QUESTION:
Given a list of 2D points represented as tuples of (x, y) coordinates and a main reference point, write a function `calculate_angles(list_of_points, main_point)` that calculates the angle (in degrees) between each point and the main reference point. The angle should be measured in the counter-clockwise direction from the positive x-axis to the line connecting the main reference point and the given point. The function should return a list of angles in degrees corresponding to each point in `list_of_points`, rounded to two decimal places. Assume that the input list of points is non-empty and the main reference point is distinct from the points in the list.
"""

import math

def calculate_angles(list_of_points, main_point):
    return [round(math.degrees(math.atan2(point[1] - main_point[1], point[0] - main_point[0])) % 360, 2) if math.degrees(math.atan2(point[1] - main_point[1], point[0] - main_point[0])) >= 0 else round(math.degrees(math.atan2(point[1] - main_point[1], point[0] - main_point[0])) + 360, 2) for point in list_of_points]