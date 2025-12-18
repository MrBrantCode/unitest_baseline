"""
QUESTION:
Write a function `compute_combination(n, r)` that calculates the number of ways to select `r` items from a list of `n` distinct options, where the order of selection does not matter. The function should take two integers `n` and `r` as input and return the number of combinations as an integer. Assume that `r` is always less than or equal to `n`.
"""

import math

def entance(n, r):
    """
    Compute the number of ways for a host to select 'r' items from
    a list of 'n' options.

    Parameters
    ----------
    n : int
        The total number of items
    r : int
        The number of items to select

    Returns
    -------
    num : int
        The number of ways to select
    """
    num = 1

    # Calculate combination
    for i in range(r):
        num *= n - i
    num //= math.factorial(r)
    
    return num