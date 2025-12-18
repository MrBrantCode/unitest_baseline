"""
QUESTION:
Create a function `calculate_patch_intrinsics` that calculates the intrinsic camera matrix for a patch of an image. The function should take as input the original intrinsic camera matrix, the top-left x and y coordinates of the patch (in pixel units), and the patch width and height. The function should return the intrinsic camera matrix for the patch, which has the same parameters as the original matrix except for the principal points `c_x` and `c_y`, which are equal to the original ones subtracted by the top-left x and y coordinates of the patch, respectively.
"""

import numpy as np

def calculate_patch_intrinsics(K, x, y, patch_width, patch_height):
    """
    Calculate the intrinsic camera matrix for a patch of an image.

    Args:
    K (numpy array): The original intrinsic camera matrix.
    x (int): The top-left x coordinate of the patch (in pixel units).
    y (int): The top-left y coordinate of the patch (in pixel units).
    patch_width (int): The width of the patch.
    patch_height (int): The height of the patch.

    Returns:
    numpy array: The intrinsic camera matrix for the patch.
    """
    # Create a copy of the original intrinsic camera matrix
    K_patch = K.copy()
    
    # Update the principal points c_x and c_y
    K_patch[0, 2] -= x
    K_patch[1, 2] -= y
    
    return K_patch