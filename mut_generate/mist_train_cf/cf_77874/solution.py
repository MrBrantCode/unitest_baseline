"""
QUESTION:
Write a function `rotate_point` that takes as input a 2D array `image`, a point `(x, y)`, and an `angle` in degrees, and returns the coordinates `(xrot, yrot)` of the point `(x, y)` after rotating the image by the given angle. The rotation is performed around the center of the image, and the result should be rounded to the nearest integer as pixel coordinates are integers.
"""

import numpy as np

def rotate_point(image, x, y, angle):
    """
    Rotate a point (x, y) in a 2D image by a given angle.

    Args:
    image (2D array): The input image.
    x (int): The x-coordinate of the point.
    y (int): The y-coordinate of the point.
    angle (float): The angle of rotation in degrees.

    Returns:
    tuple: The coordinates (xrot, yrot) of the point after rotation.
    """
    theta_rad = np.radians(angle)
    c, s = np.cos(theta_rad), np.sin(theta_rad)
    rotation_matrix = np.array(((c, -s), (s, c)))

    center = np.array(image.shape) / 2
    diff = np.array([x, y]) - center
    new_diff = np.dot(rotation_matrix, diff)
    xrot, yrot = center + new_diff

    return int(round(xrot)), int(round(yrot))