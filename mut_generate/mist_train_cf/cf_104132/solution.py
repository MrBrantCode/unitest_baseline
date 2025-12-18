"""
QUESTION:
Write a function named `weighted_average` that calculates the weighted average of a list of numbers and their corresponding weights. The function should take two lists as input: `numbers` and `weights`. The function should return the weighted average as a float. The weighted average is calculated by multiplying each number by its corresponding weight, summing up the products, and dividing by the total sum of weights. Assume that the input lists are of the same length and the sum of weights is non-zero.
"""

def weighted_average(numbers, weights):
    """
    Calculate the weighted average of a list of numbers and their corresponding weights.

    Args:
        numbers (list): A list of numbers.
        weights (list): A list of weights corresponding to the numbers.

    Returns:
        float: The weighted average.
    """
    # Calculate the total sum of all the weights
    total_sum_of_weights = sum(weights)

    # Multiply each number by its corresponding weight and sum up the products
    sum_of_products = sum(num * weight for num, weight in zip(numbers, weights))

    # Divide the sum of products by the total sum of weights
    weighted_average = sum_of_products / total_sum_of_weights

    return weighted_average