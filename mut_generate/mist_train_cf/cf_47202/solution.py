"""
QUESTION:
Reconstruct a dataset of 12,000 grayscale images, each with a size of 24x24, into a 4-dimensional tensor. The resulting tensor should be compatible with a Capsule Network model. The input is a list of 2D numpy arrays representing the images. The output tensor should have a shape of (12000, 24, 24, 1).
"""

import numpy as np

def reconstruct_dataset(images):
    """
    Reconstruct a dataset of 12,000 grayscale images, each with a size of 24x24, 
    into a 4-dimensional tensor compatible with a Capsule Network model.

    Args:
        images (list): A list of 2D numpy arrays representing the images.

    Returns:
        np.ndarray: A 4D tensor of shape (12000, 24, 24, 1)
    """
    # Convert the list of images into a numpy array
    images_np = np.array(images)

    # Reshape the numpy array to the desired shape
    images_np = images_np.reshape((12000, 24, 24, 1))

    return images_np