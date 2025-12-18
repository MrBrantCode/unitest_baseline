"""
QUESTION:
Write a function `sum_of_primes_in_range` that calculates the sum of all prime numbers between a given range. The function should take two parameters, `start` and `end`, representing the start and end of the range (inclusive). The function should return the sum of all prime numbers in the given range.
"""

def sum_of_primes_in_range(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    return sum(num for num in range(start, end + 1) if is_prime(num))