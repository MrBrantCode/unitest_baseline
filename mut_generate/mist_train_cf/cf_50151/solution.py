"""
QUESTION:
Implement the function `largest_prime_factor(n)` that returns the largest prime factor of a given integer `n`. The input `n` can be positive or negative, but `abs(n)` must be greater than 1 and not a prime number. The function should efficiently find the prime factors of `n`.
"""

def largest_prime_factor(n: int):
    """
    Returns the largest prime factor of a given integer n.
    The input n can be positive or negative, but abs(n) must be greater than 1 and not a prime number.
    
    :param n: The input integer.
    :return: The largest prime factor of n.
    """
    
    def is_prime(num: int):
        """
        Helper function to check if a number is prime.
        
        :param num: The number to check.
        :return: True if num is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = abs(n)
    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
            if n == 1:
                break
    return max(factors)