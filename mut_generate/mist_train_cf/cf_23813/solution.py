"""
QUESTION:
Write a function `calculate_entropy(distribution)` to compute the entropy of a given probability distribution. The function should take a list of probabilities as input and return the calculated entropy. The entropy should be calculated using the base 2 logarithm. The probabilities in the input list are represented as decimal numbers and are guaranteed to be non-negative and sum up to 1.
"""

import math

def calculate_entropy(distribution):
    """
    This function calculates the entropy of a given probability distribution.
    
    Parameters:
    distribution (list): A list of probabilities.
    
    Returns:
    float: The calculated entropy.
    """
    return -sum([p * math.log2(p) for p in distribution if p > 0])