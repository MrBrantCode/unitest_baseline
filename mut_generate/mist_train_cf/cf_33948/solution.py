"""
QUESTION:
Write a function `normalize_image` that takes a 2D numpy array `meanSubtractedImage` as input and returns the normalized image using the formula: `meanSubtractedImage / sqrt(sum(meanSubtractedImage^2))`. The input `meanSubtractedImage` is a 2D numpy array (n x m) where n and m are the dimensions of the image. The function should return a 2D numpy array representing the normalized image.
"""

import numpy as np

def normalize_image(meanSubtractedImage: np.ndarray) -> np.ndarray:
    return np.divide(meanSubtractedImage, np.sqrt(np.sum(np.power(meanSubtractedImage, 2))))