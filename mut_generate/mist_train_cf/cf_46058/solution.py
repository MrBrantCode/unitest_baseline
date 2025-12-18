"""
QUESTION:
Design a softmax function named `softmax` that takes a 1D numpy array of numbers (logits) as input and returns a vector representing the probability distribution of the input numbers, ensuring numerical stability by handling very small and large numbers correctly.
"""

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)