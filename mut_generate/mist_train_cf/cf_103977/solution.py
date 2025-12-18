"""
QUESTION:
Write a function `convert_to_polar(x, y)` that converts a given 2D point with coordinates (x, y) to its polar representation (r, θ), where r is the distance from the origin and θ is the angle formed by the point and the positive x-axis. The function should handle cases where x is zero or negative. The coordinates x and y are integers between -1000 and 1000, inclusive. The function should meet the following complexity requirements: Time Complexity: O(1), Space Complexity: O(1).
"""

import math

def convert_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    
    if x < 0:
        theta += math.pi
    
    return (r, theta)