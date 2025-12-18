"""
QUESTION:
Define a function `expected_distinct_toys(n, t)` that calculates the expected number of distinct toy types collected after `t` tries, given `n` types of toys. The function should return a float value representing the expected number of distinct toys.

The function should be based on the formula `E = n * (1 - ((n - 1)/n)^t)`. 

Restrictions: `n` and `t` are positive integers.
"""

def expected_distinct_toys(n, t):
    """
    Calculate the expected number of distinct toy types collected after t tries, given n types of toys.

    Args:
    n (int): The number of types of toys.
    t (int): The number of tries.

    Returns:
    float: The expected number of distinct toys.
    """
    return n * (1 - ((n - 1)/n)**t)