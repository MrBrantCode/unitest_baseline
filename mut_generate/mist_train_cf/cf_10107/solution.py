"""
QUESTION:
Write a function called `shannon_entropy` to calculate the Shannon entropy of a given probability distribution. The function should take a list of probabilities as input, where each probability is a number between 0 and 1, and the probabilities sum up to 1. The function should return the Shannon entropy of the given distribution, calculated as - Σ (pi * log2(pi)), where pi represents the probability of each event.
"""

import math

def shannon_entropy(probabilities):
    """
    Calculate the Shannon entropy of a given probability distribution.

    Args:
    probabilities (list): A list of probabilities where each probability is a number between 0 and 1,
                          and the probabilities sum up to 1.

    Returns:
    float: The Shannon entropy of the given distribution.
    """
    entropy = 0
    for probability in probabilities:
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy