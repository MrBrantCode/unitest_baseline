"""
QUESTION:
Write a function `categorize_numbers(numbers)` that takes a list of integers as input and returns two separate lists: one containing prime numbers and the other containing non-prime numbers.
"""

def categorize_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in numbers if is_prime(x)]
    non_primes = [x for x in numbers if not is_prime(x)]
    return primes, non_primes