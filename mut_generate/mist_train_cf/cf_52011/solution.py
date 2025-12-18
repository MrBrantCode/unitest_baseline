"""
QUESTION:
Create a function named `rotate` that takes a 10x10 2D array with a diagonal pattern of ones and zeros as input and returns the array rotated 90 degrees clockwise. The input array should have ones on its diagonal and zeros elsewhere. The function should use numpy's rot90 function and rotate the array clockwise.
"""

import numpy as np

def rotate(arr):
    return np.rot90(arr, 3)