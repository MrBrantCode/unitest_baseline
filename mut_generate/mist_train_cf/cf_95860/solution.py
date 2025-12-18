"""
QUESTION:
Write a function `find_second_highest_prime(numbers)` that finds the second highest prime number in a list of integers, excluding any prime numbers that are divisible by 5. The function should return `None` if there are fewer than two prime numbers in the list that meet the criteria.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_second_highest_prime(numbers):
    primes = [num for num in numbers if is_prime(num) and num % 5 != 0]
    primes.sort()
    return primes[-2] if len(primes) >= 2 else None