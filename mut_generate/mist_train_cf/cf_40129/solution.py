"""
QUESTION:
Implement a function `peak_intensity_value(image)` that takes a 2D numpy array `image` representing a grayscale image as input, where each element represents the intensity value of a pixel. The function should return the intensity value that corresponds to the peak count in the intensity histogram. The input image will always be a valid 2D numpy array representing a grayscale image, and there will be a unique peak intensity value in the histogram.
"""

import numpy as np

def peak_intensity_value(image):
    # Flatten the 2D image array into a 1D array
    flattened_image = image.flatten()
    
    # Calculate the intensity histogram using numpy's histogram function
    hist, bin_edges = np.histogram(flattened_image, bins=range(256))
    
    # Find the intensity value that corresponds to the peak count in the histogram
    peak_intensity = np.argmax(hist)
    
    return peak_intensity