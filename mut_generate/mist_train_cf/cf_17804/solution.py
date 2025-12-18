"""
QUESTION:
Implement a function `contains_two_odd_primes` that checks whether a given array contains at least two odd numbers that are also prime numbers. The function should return `True` if such numbers exist, and `False` otherwise. The function should take an array of integers as input and return a boolean value.
"""

def contains_two_odd_primes(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                return False
        return True

    odd_prime_count = 0
    for num in arr:
        if num > 1 and num % 2 != 0 and is_prime(num):
            odd_prime_count += 1
            if odd_prime_count >= 2:
                return True
    return False