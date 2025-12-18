"""
QUESTION:
Write a function `hash_distribution` that calculates and returns the distribution of perfect squares hashed into four buckets (0,1,2,3) using the hash function h(x) = x mod 4. The function should take one argument `n`, the number of perfect squares to hash. The function should return a dictionary with the bucket numbers as keys and the number of entries in each bucket as values. Assume that the input `n` is a positive integer.
"""

def hash_distribution(n):
    """
    Calculates and returns the distribution of perfect squares hashed into four buckets (0,1,2,3) using the hash function h(x) = x mod 4.
    
    Args:
    n (int): The number of perfect squares to hash.
    
    Returns:
    dict: A dictionary with the bucket numbers as keys and the number of entries in each bucket as values.
    """
    buckets = {0:0, 1:0, 2:0, 3:0}
    for i in range(1, n+1):
        h = (i**2) % 4
        buckets[h] += 1
    return buckets