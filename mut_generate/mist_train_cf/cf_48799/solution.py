"""
QUESTION:
Write a function `softmax` that takes a 1D numpy array of arbitrary real-valued scores and returns a 1D numpy array of values between zero and one which sums to 1. 

Additionally, create a function `softmax_grad` that takes a 1D softmax output and returns the derivative of the softmax function with respect to the logit being input to it.
"""

import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))   # subtract max value for numerical stability
    return e_x / e_x.sum(axis=0)

def softmax_grad(softmax):
    # Reshape the 1-d softmax to 2-d so that np.dot will do the matrix multiplication
    s = softmax.reshape(-1,1)
    return np.diagflat(s) - np.dot(s, s.T)