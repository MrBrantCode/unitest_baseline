"""
QUESTION:
Write a function `select_odd` to calculate the number of ways to select 3 items from a list of 8 options, ensuring that at least one of the items is an odd-numbered option.
"""

import itertools

def select_odd(n):
    """
    Calculate the number of ways to select 3 items from a list of n options, 
    ensuring that at least one of the items is an odd-numbered option.

    Args:
        n (int): The number of options.

    Returns:
        int: The number of ways to select 3 items ensuring that at least one of them is an odd number.
    """
    options = list(range(1, n + 1))
    combinations = list(itertools.combinations(options, 3))
    return sum(1 for comb in combinations if any(i % 2 != 0 for i in comb))