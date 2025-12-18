"""
QUESTION:
Write a function `compute_entropy(prob_dist)` that takes a dictionary `prob_dist` representing a probability distribution as input and returns its Shannon entropy. The function should check if the input probability distribution is valid (i.e., the probabilities sum up to 1) and return an error message if it's not. The function should handle large probability distributions efficiently.
"""

import math

def compute_entropy(prob_dist):
    # Check if probabilities sum up to 1
    if abs(sum(prob_dist.values()) - 1) > 1e-9:
        return "Invalid probability distribution"

    entropy = 0
    for prob in prob_dist.values():
        if prob > 0:
            entropy -= prob * math.log2(prob)

    return entropy