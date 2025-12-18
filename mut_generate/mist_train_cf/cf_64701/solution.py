"""
QUESTION:
Write a function called `sum_primes(n)` that calculates the sum of all prime numbers less than a given positive integer `n`. The function should return the aggregated sum. The function must handle cases where `n` is less than or equal to 1, in which case it should return 0.
"""

def sum_primes(n):
    """Function to compute the sum of all prime numbers less than n.
    """
    def is_prime(num):
        """Function to check if a number is prime or not.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sum(i for i in range(2, n) if is_prime(i))