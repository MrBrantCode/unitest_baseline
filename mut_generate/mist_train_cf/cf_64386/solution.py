"""
QUESTION:
Design a multiplicative hash function for a string by choosing a suitable multiplier. The multiplier should be an odd number, preferably a prime number not close to a power of 2, and should not be too large or too small. Consider the characteristics of the input keys and the size of the hash table when selecting the multiplier.
"""

def multiplicative_hash(s, p=31, m=10**9 + 7):
    """
    Computes the multiplicative hash value for a given string s.

    Args:
    s (str): The input string.
    p (int): The multiplier (default is 31).
    m (int): The modulus (default is 10^9 + 7).

    Returns:
    int: The hash value of the input string.
    """
    hash_value = 0
    p_pow = 1
    for char in s:
        hash_value = (hash_value + ord(char) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value