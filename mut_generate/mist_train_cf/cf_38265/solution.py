"""
QUESTION:
Implement a function `generate_rotation_matrices` that takes an array of angles in radians as input and returns a 3D array of 2x2 rotation matrices. Each 2D matrix in the 3D array represents the rotation by the corresponding angle in the input array. The function should follow the rotation matrix formula:

| cos(θ)  -sin(θ) |
| sin(θ)   cos(θ) |

The input is an array of angles in radians, and the output is a 3D NumPy array of rotation matrices.
"""

import numpy as np

def generate_rotation_matrices(angles):
    num_angles = len(angles)
    rotation_matrices = np.zeros((num_angles, 2, 2))
    cos_theta = np.cos(angles)
    sin_theta = np.sin(angles)
    
    rotation_matrices[:, 0, 0] = cos_theta
    rotation_matrices[:, 1, 1] = cos_theta
    rotation_matrices[:, 0, 1] = -sin_theta
    rotation_matrices[:, 1, 0] = sin_theta
    
    return rotation_matrices