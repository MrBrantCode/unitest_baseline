"""
QUESTION:
Compute the Shannon entropy of a given probability distribution, represented by a dictionary with variable-length keys. The function should handle cases where the probability distribution is not valid (i.e., the probabilities do not sum up to 1) by returning an error message indicating that the distribution is invalid. The function name should be `compute_entropy` and it should take a dictionary `prob_dist` as input, where the keys are the outcomes and the values are their corresponding probabilities.
"""

import math

def compute_entropy(prob_dist):
    # Check if probabilities sum up to 1
    if abs(sum(prob_dist.values()) - 1) > 1e-9:
        return "Invalid probability distribution"

    entropy = 0
    for prob in prob_dist.values():
        if prob > 0:
            entropy += -prob * math.log2(prob)

    return entropy