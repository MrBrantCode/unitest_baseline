"""
QUESTION:
Create a function `projectile_motion` that calculates the maximum height reached and the total flight time of a projectile launched with an initial velocity and angle in a 2D space affected by gravity. 

The function should take as input the initial velocity `mv`, angle of launch `angle_degrees`, and acceleration due to gravity `g`. The function should use the kinematic equations to calculate the maximum height `h` and total flight time `t` and return these values. The angle should be converted from degrees to radians before being used in the calculations. Assume that the projectile is launched from the origin (0, 0) in a vacuum (no air resistance).
"""

import math

def projectile_motion(mv, angle_degrees, g):
    """
    Calculate the maximum height reached and total flight time of a projectile launched with an initial velocity and angle in a 2D space affected by gravity.

    Parameters:
    mv (float): Initial velocity
    angle_degrees (float): Angle of launch in degrees
    g (float): Acceleration due to gravity

    Returns:
    tuple: Maximum height and total flight time
    """
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate maximum height
    max_height = (mv**2 * math.sin(angle_radians)**2) / (2 * g)

    # Calculate total flight time
    total_time = (2 * mv * math.sin(angle_radians)) / g

    return max_height, total_time