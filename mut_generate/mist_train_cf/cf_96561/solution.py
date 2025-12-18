"""
QUESTION:
Create a function `convertToRadians(angle)` that takes an angle in degrees as input and returns the equivalent angle in radians. The function should have a time complexity of O(1) and a space complexity of O(1). The input angle must be within the range of -360 to 360 degrees. If the angle is outside this range, raise an exception with the error message "Angle out of range. Please provide an angle within -360 to 360 degrees."
"""

import math

def convertToRadians(angle):
    if angle < -360 or angle > 360:
        raise Exception("Angle out of range. Please provide an angle within -360 to 360 degrees.")
    radians = angle * (math.pi / 180)
    return radians