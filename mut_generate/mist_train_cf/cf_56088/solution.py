"""
QUESTION:
Write a function named `convert_to_4d_tensor` that takes a list of 2D numpy arrays representing grayscale images as input and returns a 4D numpy array. The input list contains 12,000 grayscale images of size 24x24. The function should reshape the input data into a 4D tensor with dimensions (number of images, height, width, channels), where the number of channels is 1 for grayscale images.
"""

import numpy as np

def convert_to_4d_tensor(dataset):
    return np.array(dataset).reshape(len(dataset), dataset[0].shape[0], dataset[0].shape[1], 1)