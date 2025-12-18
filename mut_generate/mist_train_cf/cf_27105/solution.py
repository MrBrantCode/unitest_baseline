"""
QUESTION:
You are given the lengths of the sides AB and BC of a right-angled triangle. Write a function `find_angle` that takes two integer inputs AB and BC, and returns the angle θ (in degrees) between sides AB and BC as a string rounded to the nearest whole number, followed by the degree symbol (°).
"""

import math

def find_angle(AB, BC):
    h = math.sqrt(pow(AB, 2) + pow(BC, 2))  
    angle = round(math.degrees(math.acos(BC / h)))  
    return str(angle) + '°'  