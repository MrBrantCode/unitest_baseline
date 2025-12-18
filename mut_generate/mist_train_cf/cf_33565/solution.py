"""
QUESTION:
Implement a method called `normalizeCoordinates` that takes in six parameters: `minX`, `maxX`, `minY`, `maxY`, `minZ`, and `maxZ`. This method should normalize the x, y, and z coordinates of points in a 3D point cloud to the specified ranges `[minX, maxX]`, `[minY, maxY]`, and `[minZ, maxZ]`, respectively. The normalization should be done independently for each coordinate axis.
"""

def normalizeCoordinates(points, minX, maxX, minY, maxY, minZ, maxZ):
    """
    Normalize the x, y, and z coordinates of points in a 3D point cloud to the specified ranges.

    Args:
        points (numpy array): A 2D numpy array where each row represents a 3D point.
        minX (float): The minimum value of the x-axis range.
        maxX (float): The maximum value of the x-axis range.
        minY (float): The minimum value of the y-axis range.
        maxY (float): The maximum value of the y-axis range.
        minZ (float): The minimum value of the z-axis range.
        maxZ (float): The maximum value of the z-axis range.

    Returns:
        numpy array: The normalized 3D point cloud.
    """
    import numpy as np

    # Calculate the ranges for each coordinate axis
    rangeX = maxX - minX
    rangeY = maxY - minY
    rangeZ = maxZ - minZ

    # Normalize x, y, and z coordinates to the specified ranges
    points[:, 0] = (points[:, 0] - np.min(points[:, 0])) * (rangeX / (np.max(points[:, 0]) - np.min(points[:, 0]))) + minX
    points[:, 1] = (points[:, 1] - np.min(points[:, 1])) * (rangeY / (np.max(points[:, 1]) - np.min(points[:, 1]))) + minY
    points[:, 2] = (points[:, 2] - np.min(points[:, 2])) * (rangeZ / (np.max(points[:, 2]) - np.min(points[:, 2]))) + minZ

    return points