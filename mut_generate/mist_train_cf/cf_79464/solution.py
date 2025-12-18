"""
QUESTION:
Find the indices of grey pixels in a 3D image array that are immediate to the left of a black pixel. The grey pixel is defined as having RGB values within +/-10 of (80, 71, 71) and the black pixel is defined as having RGB values (0, 0, 0). The image array is represented as a 3D numpy array where the last dimension represents the RGB values.
"""

import numpy as np

def entrance(img):
    # Find where the image is gray (with +/-10 tolerance)
    is_grey = np.all(np.abs(img - (80, 71, 71)) < 10, axis=-1)

    # Shift the image to the left
    img_shifted = np.roll(img, -1, axis=1)

    # Find where the shifted image is black
    is_black = np.all(img_shifted == (0, 0, 0), axis=-1)

    # Find where the original image is grey and the shifted image is black
    return np.where(is_grey & is_black)