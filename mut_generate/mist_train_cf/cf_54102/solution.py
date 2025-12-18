"""
QUESTION:
Define a function `probability_unique_assignment(m, n)` that calculates the probability that exactly one number is assigned to more than one person when `n` people are each randomly assigned a number from 1 to `m` with replacement, where `m` and `n` are positive integers. The function should handle the special cases where `m = n` and `m < n` separately.
"""

import math

def probability_unique_assignment(m, n):
    """
    Calculate the probability that exactly one number is assigned to more than one person 
    when n people are each randomly assigned a number from 1 to m with replacement.

    Args:
        m (int): The number of numbers to choose from (1 to m).
        n (int): The number of people.

    Returns:
        float: The probability of exactly one number being assigned to more than one person.
    """

    # Handle special case where m = n
    if m == n:
        return 0.0
    
    # Handle special case where m < n
    if m < n:
        return 1.0
    
    # Calculate the probability
    probability = 0.0
    for k in range(2, n + 1):
        probability += math.comb(m, 1) * math.comb(n, k) * (m - 1) ** (n - k)
    
    return probability / (m ** n)