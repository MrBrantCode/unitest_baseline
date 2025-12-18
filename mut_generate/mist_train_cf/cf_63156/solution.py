"""
QUESTION:
Write a function `is_prime(n)` that filters out prime numbers from a list of integers, including both positive and negative numbers, using a caching mechanism to reduce computation time for repeated inputs. The function should maintain a cache of prime numbers computed, so that the next time the function is invoked for a number or set of numbers, if the result is already in the cache, it isn’t computed again. The function should only consider positive numbers and handle negative numbers by returning False.
"""

def is_prime(n, cache={}):
    """
    Filters out prime numbers from a list of integers, including both positive and negative numbers, 
    using a caching mechanism to reduce computation time for repeated inputs.

    Args:
        n (int): The number to check for primality.
        cache (dict): A dictionary to store computed prime numbers (default is an empty dictionary).

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    if n in cache:
        return cache[n]
    if n < 2:
        cache[n] = False
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            cache[n] = False
            return False
    cache[n] = True
    return True