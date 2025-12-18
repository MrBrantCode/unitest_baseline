"""
QUESTION:
Given a set of 2n balls, each of n different colors, where for each color there is one heavy ball and one light ball, determine the minimum number of weighings on a beam balance required to identify all the heavy balls. The heavy balls all have the same weight, and the light balls all have the same weight.
"""

def min_weighings(n):
    """
    Calculate the minimum number of weighings required to identify all heavy balls.

    Args:
    n (int): The number of different colors (or pairs of balls).

    Returns:
    int: The minimum number of weighings required.
    """
    return n