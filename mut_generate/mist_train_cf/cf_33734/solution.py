"""
QUESTION:
Write a Python function `calculate_derivatives` that takes in a 2x2 NumPy array `ACC` representing the acceleration of the joints in a two-joint arm system and returns a list containing the first and second derivatives of the joints. The first column of `ACC` corresponds to the first joint and the second column corresponds to the second joint. The output list should contain the first derivative of the first joint, first derivative of the second joint, second derivative of the first joint, and second derivative of the second joint, in that order.
"""

import numpy as np

def calculate_derivatives(ACC):
    a1d, a2d = ACC[:, 0]
    a1dd, a2dd = ACC[:, 1]
    return [a1d, a2d, a1dd, a2dd]