"""
QUESTION:
Design a function called `find_primes` that takes an integer `limit` as input and returns a list of all prime numbers up to the given `limit`.
"""

def find_primes(limit):
    """
    @brief: Finds all prime numbers up to a given limit n
    @param limit: the upper limit to find prime numbers
    @return: a list of all prime numbers found
    """
    primes = []
    for n in range(2, limit + 1):
        is_prime = True
        for prime in primes:
            if n % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes