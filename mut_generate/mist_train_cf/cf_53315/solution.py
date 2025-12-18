"""
QUESTION:
Implement a function `sieveOfEratosthenes` that takes an integer `n` as input and returns a list of all prime numbers from 2 to `n` using the Sieve of Eratosthenes algorithm. The function should only use a boolean array to keep track of prime numbers.
"""

def sieveOfEratosthenes(n):
    """
    Returns a list of all prime numbers from 2 to n using the Sieve of Eratosthenes algorithm.

    Args:
    n (int): The upper limit for finding prime numbers.

    Returns:
    list: A list of prime numbers from 2 to n.
    """
    prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return [i for i in range(2, n + 1) if prime[i]]