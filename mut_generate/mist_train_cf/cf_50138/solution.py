"""
QUESTION:
Write a function `update_weights` that takes in two parameters: `error_rate` (a float between 0 and 1) and `incorrectly_classified` (a boolean indicating whether an instance was correctly or incorrectly classified). The function should return the updated weight, using the AdaBoost weight update rule. The updated weight should be the original weight (1.0) multiplied by exp(alpha) if the instance was incorrectly classified, where alpha is calculated as 0.5 * log((1 - error_rate) / error_rate).
"""

import math

def update_weights(error_rate, incorrectly_classified):
    """
    Update the weight using the AdaBoost weight update rule.

    Args:
    error_rate (float): A float between 0 and 1 representing the error rate.
    incorrectly_classified (bool): A boolean indicating whether an instance was correctly or incorrectly classified.

    Returns:
    float: The updated weight.
    """
    alpha = 0.5 * math.log((1 - error_rate) / error_rate)
    if incorrectly_classified:
        return 1.0 * math.exp(alpha)
    else:
        return 1.0