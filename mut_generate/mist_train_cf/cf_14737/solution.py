"""
QUESTION:
Construct a function `get_primes` that returns a list of distinct prime numbers within a specified range. The function should take two query parameters, `start` and `end`, with default values of 2 and 100, respectively. The returned list should be in ascending order.
"""

def get_primes(start=2, end=100):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in range(start, end+1) if is_prime(i)]
    distinct_primes = list(set(primes))
    distinct_primes.sort()
    
    return distinct_primes