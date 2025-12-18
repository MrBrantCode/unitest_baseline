"""
QUESTION:
Create a function `odds_likelihood_difference` that takes in a probability value (between 0 and 1) and returns the odds of the event occurring. Explain in comments how odds and likelihood are related and why odds are not a type of conditional probability. Ensure that the function accurately calculates the odds given the probability and includes a conditional statement to handle the edge case where the probability is 0 or 1.
"""

def odds_likelihood_difference(probability):
    """
    Calculate the odds of an event occurring given its probability.

    Args:
        probability (float): The probability of the event occurring, between 0 and 1.

    Returns:
        float: The odds of the event occurring.
    """
    # Check for edge cases where probability is 0 or 1
    if probability == 0:
        # If probability is 0, odds are 0
        return 0
    elif probability == 1:
        # If probability is 1, odds are infinity
        return float('inf')
    else:
        # Calculate the odds as the ratio of probability to 1 - probability
        odds = probability / (1 - probability)
        return odds