"""
QUESTION:
Implement a function called "delay_gaussian" that takes two parameters: delay and ntaps. The function should apply a Gaussian function with the given delay and return a list of values representing the result. The Gaussian function should be normalized to ensure the sum of its values equals 1. The input parameter "delay" represents the mean of the Gaussian function, and "ntaps" represents the number of points at which the Gaussian function is evaluated.
"""

import numpy as np

def delay_gaussian(delay, ntaps):
    t = np.linspace(-3, 3, ntaps)
    gaussian = np.exp(-0.5 * (t - delay) ** 2)
    normalized_gaussian = gaussian / np.sum(gaussian)  # Normalize the Gaussian
    return normalized_gaussian