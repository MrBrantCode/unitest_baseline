"""
QUESTION:
Design a function named `prime_pairs` that takes a prime number `Y` as input and returns all pairs of positive integers `(A, B)` where `A` and `B` are coprime and their product equals `Y`. Note that `A` and `B` should be in the range from 1 to `Y`.
"""

import math

def prime_pairs(Y):
    """
    This function generates all pairs of positive integers (A, B) 
    where A and B are coprime and their product equals Y.

    Args:
        Y (int): A prime number.

    Returns:
        list: A list of tuples, where each tuple contains a pair of coprime numbers.
    """
    pairs = []
    for A in range(1, Y+1):
        if Y % A == 0:
            B = Y // A
            if math.gcd(A, B) == 1:
                pairs.append((A, B))
    return pairs