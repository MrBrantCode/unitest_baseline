"""
QUESTION:
Write a function `calculate_weighted_average` that calculates the weighted average of a list of numbers given their corresponding weights. The function should handle lists that may contain negative numbers, decimal numbers, repeated numbers, and may be empty. It should also take into account the weights for each number and be efficient for large lists. If the list is empty, return 0. The function should accept two parameters: `numbers` and `weights`, both of which are lists of numbers.
"""

def calculate_weighted_average(numbers, weights):
    """
    Calculate the weighted average of a list of numbers given their corresponding weights.

    Args:
        numbers (list): A list of numbers.
        weights (list): A list of weights corresponding to the numbers.

    Returns:
        float: The weighted average of the numbers. If the list is empty, returns 0.
    """
    total_score = sum(num * weight for num, weight in zip(numbers, weights))
    total_weight = sum(weights)
    
    if total_weight == 0:
        return 0
    
    weighted_average = total_score / total_weight
    return weighted_average