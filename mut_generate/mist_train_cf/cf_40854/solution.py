"""
QUESTION:
Implement the `apply_logistic_function` function, which applies the logistic function `f(x) = 1 / (1 + e^(-x))` to each element of the input array. The function should take a numpy array as input and return a new numpy array with the logistic function applied to each element. Do not use any external libraries or functions to directly compute the logistic function.
"""

import numpy as np

def apply_logistic_function(input_array: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-input_array))