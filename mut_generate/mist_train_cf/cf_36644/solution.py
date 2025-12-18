"""
QUESTION:
Implement the function `get_rays_tourism` that takes four parameters: `H` (height), `W` (width), `kinv` (intrinsic matrix inverse), and `pose` (pose matrix), and returns the origin (`rays_o`) and direction (`rays_d`) of the rays. The function should calculate the pixel coordinates, multiply them with `kinv.T` to get the ray directions, and obtain the ray origins by broadcasting the translation component of the pose matrix. The output should be in the form of two arrays: `rays_o` and `rays_d`, representing the origin and direction of the rays respectively.
"""

import numpy as np

def get_rays_tourism(H, W, kinv, pose):
    i, j = np.meshgrid(np.arange(W), np.arange(H))
    pixel_coords = np.stack((i, j, np.ones_like(i)), axis=-1)
    pixel_coords = pixel_coords.reshape(-1, 3)
    rays_d = np.dot(pixel_coords, kinv.T)
    rays_o = np.broadcast_to(pose[:3, 3], (rays_d.shape[0], 3))
    return rays_o, rays_d