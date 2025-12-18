"""
QUESTION:
Write a Python function named `softmax` that calculates the softmax of a given input vector and temperature parameter. The function should take two parameters: `x` (a list of numbers representing the input vector) and `T` (the temperature parameter). The function should return a list of probabilities, where each probability is the softmax of the corresponding element in the input vector, scaled by the temperature parameter.
"""

import math

def softmax(x, T):
    """
    This function calculates the softmax of a given input vector and temperature parameter.
    
    Parameters:
    x (list): A list of numbers representing the input vector.
    T (float): The temperature parameter.
    
    Returns:
    list: A list of probabilities, where each probability is the softmax of the corresponding element in the input vector, scaled by the temperature parameter.
    """
    
    # Calculate the exponential of each element in the input vector, scaled by the temperature parameter
    exp_x = [math.exp(i/T) for i in x]
    
    # Calculate the sum of the exponentials
    sum_exp_x = sum(exp_x)
    
    # Calculate the softmax of each element in the input vector
    softmax_x = [i / sum_exp_x for i in exp_x]
    
    return softmax_x