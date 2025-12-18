"""
QUESTION:
Implement a function named `temperature_softmax` that calculates the temperature-adjusted softmax distribution. The function should take in a 2D array `logits` representing the raw model outputs and a scalar `temperature` that controls the distribution of the outputs. The function should return a 2D array of the same shape as `logits`, where each row represents the probability distribution for a given input. The `temperature` parameter should be a positive value that affects the entropy of the output distribution.
"""

import numpy as np

def temperature_softmax(logits, temperature):
    """
    This function calculates the temperature-adjusted softmax distribution.
    
    Parameters:
    logits (2D array): Raw model outputs
    temperature (float): A positive value that controls the distribution of the outputs
    
    Returns:
    A 2D array of the same shape as logits, where each row represents the probability distribution for a given input
    """
    # Calculate the temperature-adjusted logits
    temp_logits = logits / temperature
    
    # Calculate the temperature-adjusted softmax distribution
    temp_softmax = np.exp(temp_logits) / np.sum(np.exp(temp_logits), axis=1, keepdims=True)
    
    return temp_softmax