"""
QUESTION:
Compute the function `max_money` that takes two prime numbers `A` and `B` as input and returns the maximum amount of money `X` that can be obtained using only coins of denomination `A` and `B`, given that `X` is less than or equal to 79 and `A` and `B` are less than or equal to `X`.
"""

def max_money(A, B):
    """
    Compute the maximum amount of money X that can be obtained using only coins of denomination A and B.

    Parameters:
    A (int): The denomination of the first coin.
    B (int): The denomination of the second coin.

    Returns:
    int: The maximum amount of money X that can be obtained.
    """
    max_value = 79
    max_X = 0
    for i in range(max_value // A + 1):
        for j in range(max_value // B + 1):
            X = A * i + B * j
            if X <= max_value and X > max_X:
                max_X = X
    return max_X