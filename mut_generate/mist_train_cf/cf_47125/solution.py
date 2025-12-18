"""
QUESTION:
Write a recursive function `find_primes` that takes a lower bound `low` and an upper bound `high` as input and returns a list of prime numbers between `low` and `high` (inclusive). Use a helper function `is_prime` to check if a number is prime. The `is_prime` function should take an integer `n` and an optional parameter `i` (defaulting to 2) and return `True` if `n` is prime and `False` otherwise.
"""

def find_primes(low, high):
    def is_prime(n, i=2):
        # base cases
        if n <= 2:
            return True if (n == 2) else False
        if n % i == 0:
            return False
        if i * i > n:
            return True

        # recursive case
        return is_prime(n, i + 1)

    # base case
    if low > high:
        return []

    # recursive case
    primes = []
    if is_prime(low):
        primes.append(low)
    return primes + find_primes(low+1, high)