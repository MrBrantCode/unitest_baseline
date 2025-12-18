"""
QUESTION:
Implement the `extract_class_balanced_patches` function to extract class-balanced patches from input full images. The function should take in `full_images` as a numpy array with shape [batch, height, width, image_channels], `patch_shape` as a tuple of two integers representing the height and width of the patches to be extracted, and `num_channels` as an integer representing the number of channels in the output patches. The function should return two numpy arrays: `patches` with shape [batch, example_size..., image_channels] containing the class-balanced patches, and `labels` with shape [batch, example_size] containing the labels for the patches. The patches should be extracted in a class-balanced manner, and the label for each patch should be calculated based on its content.
"""

import numpy as np
from typing import Tuple

def extract_class_balanced_patches(full_images: np.ndarray, patch_shape: Tuple[int, int], num_channels: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Extracts class-balanced patches from full images.

    Args:
        full_images (np.ndarray): input full images with the shape [batch, height, width, image_channels]
        patch_shape (Tuple[int, int]): shape of the patches to be extracted (height, width)
        num_channels (int): number of channels in the output patches

    Returns:
        np.ndarray, np.ndarray: class-balanced patches extracted from full images with the shape [batch, example_size..., image_channels]
    """
    # Calculate the number of patches to extract
    num_patches = full_images.shape[1] // patch_shape[0] * full_images.shape[2] // patch_shape[1]

    # Initialize arrays to store the extracted patches
    patches = np.zeros((full_images.shape[0], num_patches, patch_shape[0], patch_shape[1], num_channels), dtype=full_images.dtype)
    labels = np.zeros((full_images.shape[0], num_patches), dtype=np.int32)

    # Extract class-balanced patches from each full image
    for i in range(full_images.shape[0]):
        image = full_images[i]
        patch_index = 0
        for h in range(0, image.shape[0] - patch_shape[0] + 1, patch_shape[0]):
            for w in range(0, image.shape[1] - patch_shape[1] + 1, patch_shape[1]):
                patch = image[h:h+patch_shape[0], w:w+patch_shape[1]]
                patches[i, patch_index] = patch
                labels[i, patch_index] = 0  # Replace with actual label calculation
                patch_index += 1

    return patches, labels