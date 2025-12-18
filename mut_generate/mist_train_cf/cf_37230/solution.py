"""
QUESTION:
Create a function `calculate_vertical_fov` that calculates the vertical field of view (FOV) for a camera and a projector using the formula: FOV = 2 * arctan(sensor_height / (2 * focal_length)). The function should take two arguments, sensor_height and focal_length, both in cm, and return the vertical FOV in degrees. The function should ensure that the calculated FOV value is accurate to two decimal places. 

Note: The input values should be positive and non-zero. The function should not handle invalid inputs.
"""

import math

def calculate_vertical_fov(sensor_height, focal_length):
    """
    Calculate the vertical field of view (FOV) for a camera and a projector.
    
    Args:
    sensor_height (float): The height of the sensor in cm.
    focal_length (float): The focal length in cm.
    
    Returns:
    float: The vertical FOV in degrees, accurate to two decimal places.
    """
    vertical_fov = 2 * math.degrees(math.atan(sensor_height / (2 * focal_length)))
    return round(vertical_fov, 2)