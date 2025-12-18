"""
QUESTION:
Given three 3D points `(x0,y0,z0)`, `(x1,y1,z1)`, and `(x2,y2,z2)` and their corresponding 2D projections `(x0',y0')`, `(x1',y1')`, and `(x2',y2')` on a camera view plane, write a function `find_projection_matrix` to compute the camera projection matrix that maps the 3D points to their 2D projections. Assume the camera location is unknown and no additional information is provided.
"""

import numpy as np

def find_projection_matrix(points_3d, points_2d):
    """
    Compute the camera projection matrix that maps 3D points to their 2D projections.

    Parameters:
    points_3d (numpy array): 3D points (x, y, z) in the object coordinate system.
    points_2d (numpy array): 2D points (x, y) in the camera image plane.

    Returns:
    P (numpy array): 3x4 camera projection matrix.
    """
    
    # Create the A matrix for Ax = b system of linear equations
    A = np.zeros((6, 12))
    
    for i in range(3):
        row = i * 2
        A[row, 0] = points_3d[i][0]
        A[row, 1] = points_3d[i][1]
        A[row, 2] = points_3d[i][2]
        A[row, 3] = 1
        A[row, 8] = -points_2d[i][0] * points_3d[i][0]
        A[row, 9] = -points_2d[i][0] * points_3d[i][1]
        A[row, 10] = -points_2d[i][0] * points_3d[i][2]
        A[row, 11] = -points_2d[i][0]

        A[row + 1, 4] = points_3d[i][0]
        A[row + 1, 5] = points_3d[i][1]
        A[row + 1, 6] = points_3d[i][2]
        A[row + 1, 7] = 1
        A[row + 1, 8] = -points_2d[i][1] * points_3d[i][0]
        A[row + 1, 9] = -points_2d[i][1] * points_3d[i][1]
        A[row + 1, 10] = -points_2d[i][1] * points_3d[i][2]
        A[row + 1, 11] = -points_2d[i][1]
    
    # Create the b vector for Ax = b system of linear equations
    b = np.zeros(6)
    
    for i in range(3):
        row = i * 2
        b[row] = points_2d[i][0]
        b[row + 1] = points_2d[i][1]
    
    # Solve for x in Ax = b system of linear equations
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    
    # Reshape x to form 3x4 camera projection matrix
    P = np.reshape(x, (3, 4))
    
    return P