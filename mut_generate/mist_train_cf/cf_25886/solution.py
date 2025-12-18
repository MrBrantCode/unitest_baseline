"""
QUESTION:
Given a list of outcome probabilities, write a function called `calculate_event_probability` that calculates the total probability of an event occurring. The input will be a list of float values between 0 and 1, where each value represents the probability of a specific outcome. The function should return the sum of all probabilities.
"""

def calculate_event_probability(probabilities):
    """
    Calculate the total probability of an event occurring.

    Args:
        probabilities (list): A list of float values between 0 and 1, 
            where each value represents the probability of a specific outcome.

    Returns:
        float: The sum of all probabilities.
    """
    return sum(probabilities)