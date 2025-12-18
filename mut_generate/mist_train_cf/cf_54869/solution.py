"""
QUESTION:
Create a function named `convert_to_polar` that takes a 2D point (x, y) and a point of origin (a, b) as inputs. The function should calculate and return the polar coordinates (r, theta) of the point (x, y) relative to the origin (a, b). The function should be able to accommodate changes in the origin or transformation without needing manual code modifications.
"""

import math

def convert_to_polar(x, y, a=0, b=0):
    x_prime = x - a
    y_prime = y - b
    r = math.sqrt(x_prime**2 + y_prime**2)
    theta = math.atan2(y_prime, x_prime)
    if theta < 0:
        theta += 2*math.pi
    return r, theta