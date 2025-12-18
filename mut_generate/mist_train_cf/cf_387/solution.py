"""
QUESTION:
Write a recursive function `filter_primes` that takes an array of integers as input, filters out the numbers that are both prime and divisible by 3, and returns the resulting array in descending order.
"""

def filter_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(num) and num % 3 == 0]
    return sorted(primes, reverse=True)