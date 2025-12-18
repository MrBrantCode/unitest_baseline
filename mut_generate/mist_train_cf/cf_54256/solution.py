"""
QUESTION:
Design a function `get_unique_pairs(Y, Z)` that takes two prime numbers `Y` and `Z` as inputs and generates all positive pairs `(A1, B1, A2, B2)` where `A1` and `B1` are coprime to each other and their product equals `Y`, and `A2` and `B2` are coprime and their product equals `Z`. The function should ensure that `A1` and `A2` are not the same, and similarly, `B1` and `B2` are not the same. The function should be able to handle inputs where `Y < 10^6` and `Z < 10^8`.
"""

from math import gcd

def get_unique_pairs(Y, Z):
    """
    Generates all positive pairs (A1, B1, A2, B2) where A1 and B1 are coprime to each other 
    and their product equals Y, and A2 and B2 are coprime and their product equals Z.
    
    Args:
        Y (int): A prime number.
        Z (int): A prime number.
    
    Returns:
        list: A list of tuples, where each tuple contains a pair of coprime numbers.
    """

    # Since Y and Z are prime numbers, there can only be one pair of numbers 
    # which when multiplied result in the prime number itself.
    # These pairs are 1 and the prime number.
    if Y != Z:
        return [(1, Y), (1, Z)]
    else:
        return []