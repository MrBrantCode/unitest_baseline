"""
QUESTION:
Write a function called `find_primes_below` that takes an integer `n` as input and returns a list of all prime numbers between 2 and `n` (inclusive). The input `n` is a positive integer.
"""

def find_primes_below(n):
    """This function finds all prime numbers between 2 and a given integer"""
    primes = [True] * n
    primes[0], primes[1] = False, False

    # Find prime numbers
    for i, is_prime in enumerate(primes):
      if is_prime:
        for num in range(i*i, n, i):
            primes[num] = False

    # Filter out primes
    return [i for i, prime in enumerate(primes) if prime]