"""
QUESTION:
Create a function `rectangle_properties(length, width, theta_deg)` that calculates and returns the properties of a rectangle given its length, width, and largest diagonal angle in degrees. The function should return the area of the rectangle, whether it can be a square, the length of the diagonal, the angle in radians, whether the rectangle is right-angled, and the minimum distance from one vertex to the diagonal if it is not right-angled. Use the math module for all mathematical operations.
"""

import math

def rectangle_properties(length, width, theta_deg):
    """
    Calculate and return the properties of a rectangle given its length, width, and largest diagonal angle in degrees.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        theta_deg (float): The largest diagonal angle in degrees.

    Returns:
        dict: A dictionary containing the area of the rectangle, whether it can be a square, 
              the length of the diagonal, the angle in radians, whether the rectangle is right-angled, 
              and the minimum distance from one vertex to the diagonal if it is not right-angled.
    """

    # calculate area
    area = length * width

    # check if it could be a square
    is_potentially_square = True if length == width else False

    # calculate diagonal
    diagonal = math.sqrt(length**2 + width**2)

    # convert angle to radians
    theta_rad = math.radians(theta_deg)

    # check if rectangle is right-angled
    is_right_angle = True if math.isclose(theta_rad, math.atan(width/length), abs_tol=0.0001) else False

    # distance from one vertex to diagonal in case it's not right-angled
    dist_to_diag = 0 if is_right_angle else abs(width - math.sin(theta_rad)*diagonal)

    return {
        'area': area,
        'is_potentially_square': is_potentially_square,
        'diagonal': diagonal,
        'angle_in_radians': theta_rad,
        'is_right_angle': is_right_angle,
        'min_distance_to_diagonal': dist_to_diag
    }