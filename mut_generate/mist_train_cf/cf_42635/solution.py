"""
QUESTION:
Write a function `combine_images` that takes a list of images and a tuple specifying the number of rows and columns in a grid pattern. The function combines the images into a single composite image, preserving the color information if the input images are color images, and returns the composite image. The images are represented as 3D NumPy arrays, where the dimensions are (height, width, channels).
"""

import numpy as np

def combine_images(images, size):
    h, w, c = images[0].shape
    if c == 1:  
        img = np.zeros((h * size[0], w * size[1]))
        for idx, image in enumerate(images):
            i = idx % size[1]
            j = idx // size[1]
            img[j * h:j * h + h, i * w:i * w + w] = image[:, :, 0]
        return img
    else:  
        img = np.zeros((h * size[0], w * size[1], c))
        for idx, image in enumerate(images):
            i = idx % size[1]
            j = idx // size[1]
            img[j * h:j * h + h, i * w:i * w + w, :] = image
        return img