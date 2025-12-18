"""
QUESTION:
Implement a Python function `contrastive_hebbian_learning` that takes in the following parameters: activation, current weight, expected output, learning rate (eta), learning rate decay factor (gamma), and maximum number of iterations. The function should update the weight using the Contrastive Hebbian Learning algorithm and return the updated weight. The algorithm iteratively updates the weight using the formula: weight += eta * (activation_difference - gamma * weight), where activation_difference is the outer product of the activation and expected output.
"""

import numpy as np
from typing import Union

def contrastive_hebbian_learning(activation: Union[np.ndarray, list],
                                 weight: Union[np.ndarray, list],
                                 expected: Union[np.ndarray, list],
                                 eta: float = 0.1,
                                 gamma: float = 0.1,
                                 max_iter: int = 10) -> Union[np.ndarray, list]:
    """Contrastive Hebbian Learning.

    Args:
        activation: The activation values of the neurons.
        weight: The current weight values of the connections.
        expected: The expected output values.
        eta: The learning rate (default 0.1).
        gamma: The learning rate decay factor (default 0.1).
        max_iter: The maximum number of iterations (default 10).

    Returns:
        The updated weight after performing Contrastive Hebbian Learning.
    """
    activation = np.array(activation)
    weight = np.array(weight)
    expected = np.array(expected)

    for _ in range(max_iter):
        activation_difference = np.outer(activation, expected)
        weight += eta * (activation_difference - gamma * weight)

    return weight