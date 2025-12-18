"""
QUESTION:
Implement the `sigmrnd` function to generate random numbers from a sigmoid distribution. The sigmoid function is defined as `1 / (1 + exp(-x))`. The function should take an input array, calculate the sigmoid values using the formula, and return the array of sigmoid values. Use the `numpy` library for mathematical operations.
"""

import numpy as np

def sigmrnd(input):
    # Calculate the sigmoid values using the input array
    sigmoid_values = 1 / (1 + np.exp(-input))
    
    return sigmoid_values