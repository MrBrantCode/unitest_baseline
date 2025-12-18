"""
QUESTION:
Write a function `first_non_repeating_prime` that takes an array of integers as input and returns the first non-repeating prime number in the array. The array may contain both positive and negative integers, and may also contain duplicate elements. If there are no non-repeating prime numbers, return None.
"""

def first_non_repeating_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in nums if is_prime(abs(num))]
    for prime in primes:
        if primes.count(prime) == 1:
            return prime
    return None