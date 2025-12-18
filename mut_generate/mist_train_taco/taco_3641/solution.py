"""
QUESTION:
Given a number **n**, return the number of positive odd numbers below **n**, EASY!

Expect large Inputs!
"""

def count_positive_odds(n: int) -> int:
    """
    Counts the number of positive odd numbers below the given number n.

    Parameters:
    n (int): The upper limit (exclusive) up to which to count the positive odd numbers.

    Returns:
    int: The count of positive odd numbers below n.
    """
    return len(range(1, n, 2))