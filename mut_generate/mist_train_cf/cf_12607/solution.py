"""
QUESTION:
Create a function `calculate_covariance` that takes two lists of numbers as input and returns their covariance, handling lists of different lengths. The function should compute the biased covariance.
"""

import numpy as np

def calculate_covariance(list1, list2):
    cov = np.cov(list1, list2, bias=True)[0, 1]
    return cov