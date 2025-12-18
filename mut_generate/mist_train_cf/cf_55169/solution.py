"""
QUESTION:
Write a function called `calculate_sample_weights` that takes a target population size and a list of sample weights as input. The function should return True if the sum of the sample weights equals the target population size and False otherwise. However, note that the function should also consider acceptable variance and return True if the sum of the sample weights is close to the target population size, but not necessarily exactly equal due to possible rounding errors or statistical approximation.
"""

def calculate_sample_weights(target_population_size, sample_weights):
    """
    This function checks if the sum of the sample weights equals or is close to the target population size.

    Args:
        target_population_size (int): The target population size.
        sample_weights (list): A list of sample weights.

    Returns:
        bool: True if the sum of the sample weights equals or is close to the target population size, False otherwise.
    """

    # Define an acceptable variance (e.g., 1%)
    acceptable_variance = 0.01

    # Calculate the sum of the sample weights
    sum_sample_weights = sum(sample_weights)

    # Check if the sum of the sample weights is within the acceptable variance of the target population size
    return abs(sum_sample_weights - target_population_size) <= (target_population_size * acceptable_variance)