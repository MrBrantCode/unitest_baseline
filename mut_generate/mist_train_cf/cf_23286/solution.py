"""
QUESTION:
Write a function named largest_prime_factor to find the largest prime factor of a given number. The function should take an integer as input and return its largest prime factor.
"""

def largest_prime_factor(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            max_prime_factor = i
    return max_prime_factor