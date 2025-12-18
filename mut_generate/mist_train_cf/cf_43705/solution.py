"""
QUESTION:
Write a function named `softmax` that takes in a list of output scores (logits) and a temperature parameter, and returns a valid probability distribution using the softmax function. The function should allow for the adjustment of the temperature parameter to control the concentration of probability mass on the logits, with lower temperatures resulting in a more concentrated distribution and higher temperatures resulting in a more uniform distribution.
"""

import math

def softmax(logits, temperature):
    """
    Compute the softmax of a list of logits with a given temperature parameter.

    Args:
    logits (list): A list of output scores.
    temperature (float): A temperature parameter to control the concentration of probability mass.

    Returns:
    list: A valid probability distribution.
    """
    # Apply the temperature to the logits
    logits_with_temp = [score / temperature for score in logits]
    
    # Compute the maximum value for stability
    max_val = max(logits_with_temp)
    
    # Compute the exponential of each logit
    exp_logits = [math.exp(score - max_val) for score in logits_with_temp]
    
    # Compute the sum of the exponentials
    sum_exp_logits = sum(exp_logits)
    
    # Compute the softmax distribution
    softmax_distribution = [exp_logit / sum_exp_logits for exp_logit in exp_logits]
    
    return softmax_distribution