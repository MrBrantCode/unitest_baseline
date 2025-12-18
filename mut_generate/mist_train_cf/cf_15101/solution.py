"""
QUESTION:
Write a function `calculate_height` that takes in the angle `θ` (theta), ratio of side lengths `R`, and velocity `V` as parameters. The function should return the calculated height `h` of a triangle using the Law of Sines and Law of Cosines, considering the effect of air resistance on the trajectory, with an acceleration due to gravity `g` of 9.81 m/s^2.
"""

import math

def calculate_height(theta, R, V):
    """
    Calculate the height of a triangle using the Law of Sines and Law of Cosines, 
    considering the effect of air resistance on the trajectory.

    Parameters:
    theta (float): The angle θ (theta) of the triangle in radians.
    R (float): The ratio of side lengths (opposite side length divided by the adjacent side length).
    V (float): The velocity of the triangle.

    Returns:
    float: The calculated height h of the triangle.
    """
    g = 9.81  # acceleration due to gravity in m/s^2
    height = (2 * R * math.sin(theta) * (V**2) * math.sin(2*theta)) / (g * (1 + (V**2) * math.sin(theta)**2 / (2 * g * R * math.cos(theta)**2) + (V**2) * math.sin(2*theta)**2 / (2 * g * R * math.cos(theta)**2)))
    return height