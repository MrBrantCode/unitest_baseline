"""
QUESTION:
Write a function `normalize_pose(pose)` that takes a 7-dimensional pose vector as input, where the first three elements represent the x, y, and z coordinates of the position, and the next four elements represent the orientation in the form of quaternions. The function should return the normalized pose vector according to the following rules: the x, y, and z coordinates remain unchanged, the orientation quaternion is normalized, and the fourth element is replaced with the cosine of half the angle represented by the original fourth element, which should be interpreted as degrees.
"""

import numpy as np

def normalize_pose(pose):
    norm_pose = np.zeros((7, ))
    norm_pose[0:3] = pose[0:3]
    norm_pose[3] = np.cos(np.deg2rad(pose[3]))
    
    # Normalize the quaternion components
    quaternion = pose[4:]
    norm_quaternion = quaternion / np.linalg.norm(quaternion)
    norm_pose[4:] = norm_quaternion
    
    return norm_pose