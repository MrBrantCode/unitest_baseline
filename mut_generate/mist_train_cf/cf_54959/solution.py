"""
QUESTION:
Write a function `discrete_random_variable_outcomes` to check whether discrete random variables are limited to numerical outcomes.
"""

def discrete_random_variable_outcomes(outcomes):
    """
    Checks whether discrete random variables are limited to numerical outcomes.

    Args:
        outcomes (list): A list of outcomes for a discrete random variable.

    Returns:
        bool: True if all outcomes are numerical, False otherwise.
    """
    return all(isinstance(outcome, (int, float)) for outcome in outcomes)