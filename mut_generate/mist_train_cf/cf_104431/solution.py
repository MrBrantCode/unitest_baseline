"""
QUESTION:
Write a function `cube_root_of_n_divisible_by_7` that takes an integer `n` as input, where `n` is between 1 and 10^9 and is divisible by 7. The function should return the cube root of `n`.
"""

def cube_root_of_n_divisible_by_7(n):
    """
    Calculate the cube root of a given integer n, where n is between 1 and 10^9 and is divisible by 7.

    Args:
        n (int): A positive integer divisible by 7.

    Returns:
        float: The cube root of n.
    """
    # calculate cube root of n using exponentiation
    cube_root = n ** (1/3)
    return cube_root