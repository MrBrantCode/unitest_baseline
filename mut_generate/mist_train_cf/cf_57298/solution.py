"""
QUESTION:
Write a function `calculate_trials` to determine the necessary number of trials in an experiment to achieve an estimate of the absolute error that strays no more than a specified error percentage from the actual absolute error with a given confidence level. The function should take two parameters: `epsilon` (the acceptable error in the probability estimate) and `delta` (the probability that the true probability lies outside the estimated probability by more than epsilon).
"""

import math

def calculate_trials(epsilon, delta):
    """
    Calculate the necessary number of trials in an experiment to achieve an estimate of the absolute error that strays no more than a specified error percentage from the actual absolute error with a given confidence level.

    Parameters:
    epsilon (float): The acceptable error in the probability estimate.
    delta (float): The probability that the true probability lies outside the estimated probability by more than epsilon.

    Returns:
    int: The minimum number of trials needed.
    """
    return math.ceil((1 / (2 * epsilon**2)) * math.log(2 / delta))