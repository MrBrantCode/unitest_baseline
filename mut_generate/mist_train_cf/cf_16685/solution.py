"""
QUESTION:
Write a function named `compute_shannon_entropy` that calculates the Shannon entropy of a given probability distribution represented as a dictionary. The function should return an error message if the probabilities in the distribution do not sum up to 1. The function should be efficient and able to handle large distributions. The input dictionary keys can be of any length and type, but the values must be numeric and represent probabilities.
"""

import math

def compute_shannon_entropy(probability_distribution):
    # Check if the probabilities sum up to 1
    total_probability = sum(probability_distribution.values())
    if not math.isclose(total_probability, 1):
        return "Invalid distribution: probabilities do not sum up to 1"

    # Compute Shannon entropy
    entropy = 0
    for probability in probability_distribution.values():
        entropy -= probability * math.log2(probability)

    return entropy