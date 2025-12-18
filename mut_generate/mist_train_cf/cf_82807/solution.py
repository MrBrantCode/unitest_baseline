"""
QUESTION:
Write a function `calculate_hfov` that takes in a Three.js camera object `cam` and returns the horizontal field of view in degrees. The function should use the vertical field of view and the aspect ratio of the camera to calculate the horizontal field of view. The vertical field of view is obtained from `cam.fov` and the aspect ratio is obtained from `cam.aspect`.
"""

import math

def calculate_hfov(cam):
    """
    Calculate the horizontal field of view in degrees.

    Args:
        cam: A Three.js camera object.

    Returns:
        The horizontal field of view in degrees.
    """
    vfov = math.radians(cam.fov)
    aspect_ratio = cam.aspect
    hfov = 2 * math.atan(math.tan(vfov / 2) * aspect_ratio)
    return math.degrees(hfov)