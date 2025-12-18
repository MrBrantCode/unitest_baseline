"""
QUESTION:
Implement a function named `softmax_with_temperature` that takes in a 1D list of numbers and a temperature parameter, applies the softmax function to the input list, and returns the resulting probability distribution. The function should be able to handle the case where the temperature parameter approaches zero.
"""

import numpy as np

def softmax_with_temperature(input_list, temperature):
    """
    Applies the softmax function to the input list with a temperature parameter.

    Args:
    input_list (list): A 1D list of numbers.
    temperature (float): The temperature parameter.

    Returns:
    list: The resulting probability distribution.
    """
    # Apply the temperature parameter to the input list
    temperature_list = np.array(input_list) / temperature

    # Apply the softmax function
    exp_list = np.exp(temperature_list - np.max(temperature_list))
    probabilities = exp_list / np.sum(exp_list)

    return probabilities.tolist()