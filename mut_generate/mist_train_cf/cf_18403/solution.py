"""
QUESTION:
Write a function `calculate_probability` that takes a list of probabilities of different outcomes and returns the probability of an event occurring, considering each outcome has a different probability and ignoring outcomes with zero probability.
"""

def calculate_probability(probabilities):
    """
    Calculate the probability of an event occurring from a list of outcome probabilities.

    Args:
    probabilities (list): A list of probabilities of different outcomes.

    Returns:
    float: The probability of the event occurring.
    """
    total_outcomes = len(probabilities)
    total_favourable_outcomes = sum(1 for prob in probabilities if prob > 0)
    probability_of_event = total_favourable_outcomes / total_outcomes
    return probability_of_event