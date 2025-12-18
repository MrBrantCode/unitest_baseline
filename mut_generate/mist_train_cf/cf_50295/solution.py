"""
QUESTION:
Implement the `calculate_entropy` function, which takes a list of probabilities as input and returns the calculated entropy value. The function should be able to handle a list of any length and should return a float value.
"""

def calculate_entropy(probabilities):
    """
    Calculate the entropy value from a list of probabilities.

    Args:
    probabilities (list): A list of probabilities.

    Returns:
    float: The calculated entropy value.
    """
    import math
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log(p, 2)
    return entropy