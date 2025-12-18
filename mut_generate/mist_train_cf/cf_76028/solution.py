"""
QUESTION:
Create a function `generate_primes(n)` that generates a list of all prime numbers between 1 and `n` (inclusive) using an optimized algorithm, and a function `sum_of_primes(primes)` that calculates the sum of the prime numbers in the list. The algorithm should have a time complexity better than O(n^2) and a space complexity of O(n).
"""

def generate_primes(n):
    """
    Generates a list of all prime numbers between 1 and n (inclusive) using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers between 1 and n (inclusive).

    Time Complexity:
        O(n log log n)

    Space Complexity:
        O(n)
    """
    prime = [True for _ in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1 

    return [p for p in range(2, n) if prime[p]]