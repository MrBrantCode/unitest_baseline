"""
QUESTION:
Implement a function called `calculate_entropy` that takes in a list of probabilities and returns the calculated entropy value. The function should use the Shannon entropy formula: -Σ(p * log2(p)) for each probability p in the list. Assume that the input list contains non-negative values that sum up to 1.
"""

import math

def calculate_entropy(probabilities):
    """
    This function calculates the entropy value from a list of probabilities.
    
    Parameters:
    probabilities (list): A list of probabilities.
    
    Returns:
    float: The calculated entropy value.
    """
    entropy = 0
    for p in probabilities:
        if p != 0:
            entropy -= p * math.log2(p)
    return entropy