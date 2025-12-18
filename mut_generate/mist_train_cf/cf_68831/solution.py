"""
QUESTION:
Convert a collection of 12,000 grayscale images of size 24x24 into a four-dimensional tensor with shape (number of images, height, width, channels), where the number of channels is 1 for grayscale images. The function should take a 3D numpy array representing the images and return a reshaped 4D tensor.
"""

import numpy as np

def convert_to_4d_tensor(images):
    return images.reshape(images.shape[0], images.shape[1], images.shape[2], 1)