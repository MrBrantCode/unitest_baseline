"""
QUESTION:
Implement a function `process_calibration_data(camera_calibrations)` that takes a list of camera calibration objects as input. Each camera calibration object contains `extrinsic.transform` (a 4x4 transformation matrix) and `intrinsic` (a list of intrinsic calibration parameters). 

The function should perform the following steps:
1. For each camera calibration object, calculate the transformation matrix `tmp` by reshaping the extrinsic transformation, converting it to a homogeneous matrix, and performing a specific matrix multiplication with a given transformation matrix `T_front_cam_to_ref`.
2. Append the first 12 elements of the resulting matrix `tmp` to a list `Tr_velo_to_cam`.
3. For each camera calibration object, create a 3x4 matrix `tmp` using the intrinsic calibration parameters and set `tmp[0, 0]`, `tmp[1, 1]`, `tmp[0, 2]`, and `tmp[1, 2]` based on the intrinsic parameters.

The function should return `Tr_velo_to_cam` and the list of intrinsic matrices.
"""

import numpy as np

def process_calibration_data(camera_calibrations, T_front_cam_to_ref):
    Tr_velo_to_cam = []

    for camera in camera_calibrations:
        tmp = np.array(camera.extrinsic.transform).reshape(4, 4)
        tmp = np.vstack((T_front_cam_to_ref, [0, 0, 0, 1])) @ np.linalg.inv(tmp)
        Tr_velo_to_cam.append(["%e" % i for i in tmp[:3, :].reshape(12)])

    intrinsic_matrices = []
    for cam in camera_calibrations:
        tmp = np.zeros((3, 4))
        tmp[0, 0] = cam.intrinsic[0]
        tmp[1, 1] = cam.intrinsic[1]
        tmp[0, 2] = cam.intrinsic[2]
        tmp[1, 2] = cam.intrinsic[3]
        intrinsic_matrices.append(tmp)

    return Tr_velo_to_cam, intrinsic_matrices