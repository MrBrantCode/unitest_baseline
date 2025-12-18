"""
QUESTION:
Write a function `calculate_probability` that takes in three intercepts (`b0`) and three coefficients (`b1`) for a multi-class logistic regression model, along with a value for `age`, and returns the probabilities for each class. Assume the model has three classes, and the coefficients are ordered as [male, non-binary, female]. The function should use the softmax function to calculate the probabilities. 

Note: The model is a multi-class logistic regression model, not a binary logistic regression model.
"""

import numpy as np

def calculate_probability(b0, b1, age):
    """
    Calculate probabilities for each class in a multi-class logistic regression model.

    Args:
    b0 (list): A list of intercepts for each class.
    b1 (list): A list of coefficients for each class.
    age (float): The input value for age.

    Returns:
    list: A list of probabilities for each class.
    """

    # Calculate the linear predictors for each class
    linear_predictors = [b0[i] + b1[i] * age for i in range(len(b0))]

    # Convert linear predictors to log-odds
    log_odds = np.exp(linear_predictors)

    # Calculate the sum of log-odds
    log_odds_sum = np.sum(log_odds)

    # Convert log-odds to probabilities using softmax function
    probabilities = log_odds / log_odds_sum

    return probabilities