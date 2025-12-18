"""
QUESTION:
Function: Locate the 2D coordinates of an image point in the world coordinate frame.

Information: 
- 3D coordinates of the image point in camera coordinate frame using the camera intrinsic parameters and the pixel coordinates of the image point
- Transformation matrix of camera in lidar coordinate frame
- 6 degrees of freedom transformation matrix of lidar in world coordinate frame

Restrictions: The function should output the 2D coordinates of an image point in the world coordinate frame P, using the provided information.
"""

import numpy as np

def locate_image_point(u, v, fx, fy, cx, cy, T_cam_lidar, T_lidar_world):
    """
    Locate the 2D coordinates of an image point in the world coordinate frame.

    Args:
    u (float): Pixel x-coordinate of the image point.
    v (float): Pixel y-coordinate of the image point.
    fx (float): Camera intrinsic parameter, focal length in x-direction.
    fy (float): Camera intrinsic parameter, focal length in y-direction.
    cx (float): Camera intrinsic parameter, principal point x-coordinate.
    cy (float): Camera intrinsic parameter, principal point y-coordinate.
    T_cam_lidar (numpy array): Transformation matrix from camera to lidar coordinate frame.
    T_lidar_world (numpy array): Transformation matrix from lidar to world coordinate frame.

    Returns:
    tuple: 2D coordinates (x, y) of the image point in the world coordinate frame.
    """

    # Image point to camera coordinate frame
    X_cam = np.array([(u - cx) / fx, (v - cy) / fy, 1.0])

    # Camera coordinate frame to lidar coordinate frame
    X_lidar = T_cam_lidar.dot(np.append(X_cam, 1.0))

    # Lidar coordinate frame to world coordinate frame
    X_world = T_lidar_world.dot(X_lidar)

    # Return 2D coordinates of image point in world coordinate frame
    return X_world[0], X_world[1]