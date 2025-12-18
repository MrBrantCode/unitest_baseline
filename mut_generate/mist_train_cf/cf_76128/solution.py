"""
QUESTION:
Calculate the entropy of a feature in a dataset and its impact on the decision-making process of classification algorithms.

Create a function called `calculate_entropy` that takes a list of probabilities as input and returns the entropy of the given probabilities. The probabilities should be non-negative and sum up to 1. The function should handle the case where the probability is 0, in which case the entropy should be 0.

Restrictions: 
- Use the Shannon entropy formula: H(p) = - ∑ p(x) log2(p(x))
- Use base 2 logarithm for the calculation.
- Use a small value to avoid division by zero error when calculating the logarithm.
"""

import math

def calculate_entropy(probabilities):
    """
    Calculate the entropy of a given list of probabilities.

    Args:
    probabilities (list): A list of probabilities. The probabilities should be non-negative and sum up to 1.

    Returns:
    float: The entropy of the given probabilities.
    """
    epsilon = 1e-15  # A small value to avoid division by zero error
    entropy = 0.0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p + epsilon)
    return entropy