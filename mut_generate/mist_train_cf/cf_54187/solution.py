"""
QUESTION:
Implement a sigmoid function in Python that maps any real number to a value within a certain range and identify the range of the output. The function should take a real number as input and return a value between the specified range. The function should be a mathematical representation of the sigmoid function S(x) = 1 / (1 + e^-x).
"""

import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))