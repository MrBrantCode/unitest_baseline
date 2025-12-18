"""
QUESTION:
Reshape a 2D or 3D dataset into a 4D tensor to serve as input for a Capsule Network. The dataset contains 12,000 grayscale images with 24x24 pixels each. The 4D tensor should have dimensions representing the number of images, image width and height (24x24), and the number of channels (1 for grayscale).
"""

import numpy as np

def reshape_dataset(dataset):
    """
    Reshape a 2D or 3D dataset into a 4D tensor to serve as input for a Capsule Network.

    Args:
        dataset (numpy array): A 2D or 3D numpy array containing grayscale images.

    Returns:
        A 4D numpy array with dimensions representing the number of images, image width and height, and the number of channels.
    """
    if len(dataset.shape) == 3:
        dataset = np.expand_dims(dataset, axis=-1)
    elif len(dataset.shape) == 2:
        dataset = dataset.reshape((-1, 24, 24))
        dataset = np.expand_dims(dataset, axis=-1)
    return dataset