"""
QUESTION:
Create a function called `convertToRadians` that takes an angle in degrees as input. The function should convert the angle to radians and return the result. If the input angle is not within the range of -360 to 360 degrees, the function should raise an exception with an error message "Angle out of range. Please provide an angle within -360 to 360 degrees." The function should have a time complexity of O(1) and a space complexity of O(1).
"""

import math

def convertToRadians(angle):
    if angle < -360 or angle > 360:
        raise Exception("Angle out of range. Please provide an angle within -360 to 360 degrees.")
    radians = angle * (math.pi / 180)
    return radians