"""
QUESTION:
Write a function named `calculate_weighted_average` that takes two lists of numbers and their corresponding weights as input and returns the weighted average. The function should calculate the weighted average using the formula: (number1 * weight1 + number2 * weight2 + ... + numberN * weightN) / (weight1 + weight2 + ... + weightN). The function should assume that the lengths of the input lists are equal, and the weights are all non-zero. The input numbers and weights are floating-point numbers between 0 and 100.
"""

def calculate_weighted_average(numbers, weights):
    """
    Calculate the weighted average of a list of numbers with corresponding weights.

    Args:
        numbers (list): A list of floating-point numbers between 0 and 100.
        weights (list): A list of non-zero weights corresponding to the numbers.

    Returns:
        float: The weighted average.
    """
    weighted_sum = sum(num * weight for num, weight in zip(numbers, weights))
    weight_sum = sum(weights)
    return weighted_sum / weight_sum