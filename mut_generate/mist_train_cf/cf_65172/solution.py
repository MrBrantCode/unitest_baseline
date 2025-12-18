"""
QUESTION:
Write a Python function `calculate_conditional_probability` to calculate the conditional probability of two binary random variables. The function should take three parameters: `p_x` (the probability of event X), `p_y` (the probability of event Y), and `p_x_given_not_y` (the conditional probability of event X given the non-occurrence of event Y).
"""

def calculate_conditional_probability(p_x, p_y, p_x_given_not_y):
    """
    Calculate the conditional probability of two binary random variables.

    Parameters:
    p_x (float): The probability of event X.
    p_y (float): The probability of event Y.
    p_x_given_not_y (float): The conditional probability of event X given the non-occurrence of event Y.

    Returns:
    float: The conditional probability of event X given event Y.
    """
    p_not_y = 1 - p_y
    p_x_and_not_y = p_x_given_not_y * p_not_y
    p_x_and_y = p_x - p_x_and_not_y
    p_x_given_y = p_x_and_y / p_y
    return p_x_given_y