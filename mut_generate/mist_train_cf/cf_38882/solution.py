"""
QUESTION:
Implement the `get_4x4_world_to_cam_mat` method to construct a 4x4 transformation matrix representing the transformation from the world coordinate system to the camera coordinate system. 

The method should utilize the following instance variables: `self._rotation_mat` (3x3 rotation matrix), `self._translation_vec` (translation vector), and `self._center` (camera center coordinates). The resulting transformation matrix should be in the standard format for homogeneous coordinates, where the last row is `[0, 0, 0, 1]`.
"""

import numpy as np

def get_4x4_world_to_cam_mat(rotation_mat, translation_vec, camera_center):
    world_to_cam_mat = np.eye(4)
    world_to_cam_mat[:3, :3] = rotation_mat
    world_to_cam_mat[:3, 3] = translation_vec
    world_to_cam_mat[3, :3] = np.dot(-camera_center, rotation_mat)  # -C*R
    return world_to_cam_mat