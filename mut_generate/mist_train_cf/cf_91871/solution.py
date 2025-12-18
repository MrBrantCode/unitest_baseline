"""
QUESTION:
Write a function named `prime_numbers` that takes two integers `start` and `end` as input, where `start` is less than `end`, and returns a list of prime numbers between `start` and `end` (inclusive). The function should not use any built-in functions or libraries that directly determine if a number is prime and should have a time complexity of O(n√m), where n is the number of integers between `start` and `end`, and m is the largest number between `start` and `end`. If `start` is less than or equal to 0, consider it as 2.
"""

import math

def prime_numbers(start, end):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    if start <= 0:
        start = 2
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes