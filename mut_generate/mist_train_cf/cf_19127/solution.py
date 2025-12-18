"""
QUESTION:
Write a function `nth_prime_from_end` that takes an integer `index` and a list of prime numbers `primes` sorted in descending order as input, and returns the prime number at the given `index` from the start of the list. Note that indexing starts at 0.
"""

def nth_prime_from_end(index, primes):
    """
    Returns the prime number at the given index from the start of the list.

    Args:
    index (int): The index of the prime number to be returned.
    primes (list): A list of prime numbers in descending order.

    Returns:
    int: The prime number at the given index.
    """
    return primes[index]