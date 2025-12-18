"""
QUESTION:
Create a function `weighted_average` that calculates the weighted average of a list of values with given weights. The function should take two parameters: `values` and `weights`, both of which are lists of the same length. The function should return the weighted average of the values. Assume that the sum of the weights is not equal to zero.
"""

def weighted_average(values, weights):
    """
    This function calculates the weighted average of a list of values with given weights.
    
    Args:
        values (list): A list of values.
        weights (list): A list of weights corresponding to the values.
    
    Returns:
        float: The weighted average of the values.
    """
    return sum(v*w for v,w in zip(values, weights)) / sum(weights)