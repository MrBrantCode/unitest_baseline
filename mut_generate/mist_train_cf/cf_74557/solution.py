"""
QUESTION:
Write a function named `weighted_average` that takes a list of numbers and a corresponding list of weights. The function should calculate the weighted average, but only if the sum of the weights is exactly 1. If the sum of the weights is not 1, the function should return "Invalid weights".
"""

def weighted_average(values, weights):
    """
    Calculate the weighted average of a list of numbers.
    
    Args:
    values (list): A list of numbers.
    weights (list): A list of weights corresponding to the numbers.
    
    Returns:
    float or str: The weighted average if the sum of the weights is 1, "Invalid weights" otherwise.
    """
    if sum(weights) != 1:
        return "Invalid weights"
    return sum(val * weight for val, weight in zip(values, weights))