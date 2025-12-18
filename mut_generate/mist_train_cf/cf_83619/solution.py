"""
QUESTION:
Implement a function `evaluate_smoothing_technique` that evaluates the choice of smoothing techniques before proceeding with regression analysis. The function should take in the original dataset and the smoothed dataset, and return a value that can be used to compare different smoothing techniques. The function should be able to handle different types of smoothing techniques, including moving averages with varying window sizes (e.g., 2-point, 3-point, 5-point).
"""

def evaluate_smoothing_technique(original_data, smoothed_data):
    """
    Evaluates the choice of smoothing techniques by calculating the mean squared error.

    Args:
        original_data (list): The original dataset.
        smoothed_data (list): The smoothed dataset.

    Returns:
        float: The mean squared error between the original and smoothed datasets.
    """
    # Calculate the mean squared error
    mse = sum((a - b) ** 2 for a, b in zip(original_data, smoothed_data)) / len(original_data)
    return mse