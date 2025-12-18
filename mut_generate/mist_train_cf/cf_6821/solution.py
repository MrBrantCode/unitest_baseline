"""
QUESTION:
Create a function named `convertToRadians` that takes an angle in degrees as input and returns its equivalent value in radians. The function should have a time complexity of O(1) and a space complexity of O(1). It must also check that the input angle is within the range of -360 to 360 degrees and raise an exception if it's not. The resulting radians should be rounded to 6 decimal places.
"""

import math

def convertToRadians(angle):
    if angle < -360 or angle > 360:
        raise Exception("Angle out of range. Please provide an angle within -360 to 360 degrees.")
    
    radians = math.radians(angle)
    rounded_radians = round(radians, 6)
    return rounded_radians