"""
QUESTION:
Write a function `find_off_circumference_point` that takes a list of two points that lie on a circle's circumference and a list of points to check as input, and returns a list of points that do not lie on the circle's circumference. Assume that the two given points on the circle's circumference are not identical and do not form a diameter, and the circle's center is not at the origin (0,0).
"""

import math

def find_off_circumference_point(pt1, pt2, pts_to_check):
    # Function to calculate midpoint
    def midpoint(pt_a, pt_b):
        return [(pt_a[0]+pt_b[0])/2, (pt_a[1]+pt_b[1])/2]

    # Function to calculate distance
    def distance(pt_a, pt_b):
        return math.sqrt((pt_a[0] - pt_b[0])**2 + (pt_a[1] - pt_b[1])**2)

    # Calculate center and radius of circle
    center = midpoint(pt1, pt2)
    radius = distance(center, pt1)

    # Check each point
    off_circumference_pts = []
    for pt in pts_to_check:
        if distance(center, pt) != radius:
            off_circumference_pts.append(pt)
    return off_circumference_pts