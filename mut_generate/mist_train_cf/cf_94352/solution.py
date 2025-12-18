"""
QUESTION:
Write a function named `compute_shannon_entropy` that takes a dictionary `probability_distribution` as input, where the keys represent variable-length values and the values represent their corresponding probabilities. The function should return the Shannon entropy of the probability distribution. If the probabilities do not sum up to 1, return an error message "Invalid distribution: probabilities do not sum up to 1". The function should be optimized to handle larger probability distributions efficiently.
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