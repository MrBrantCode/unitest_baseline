"""
QUESTION:
Transform the given dataset of 12,000 grayscale images with a resolution of 24x24 pixels into a 4-dimensional tensor. The output tensor should have dimensions representing (number_of_samples, image_height, image_width, number_of_channels). 

The function should accept a 3-dimensional numpy array (or a dataset convertible to a numpy array) as input and return a 4-dimensional numpy array. The number_of_samples is 12,000, image height and image width are both 24 pixels, and number_of_channels is 1 for grayscale images.
"""

import numpy as np

def transform_dataset(dataset):
    """
    Transform a 3-dimensional dataset of grayscale images into a 4-dimensional tensor.
    
    Parameters:
    dataset (numpy array): A 3-dimensional numpy array representing the dataset of grayscale images.
    
    Returns:
    numpy array: A 4-dimensional numpy array representing the transformed dataset.
    """
    
    # Add another dimension to transform the dataset into a 4-D tensor for the grayscale channel
    dataset = np.expand_dims(dataset, axis=-1)
    
    return dataset