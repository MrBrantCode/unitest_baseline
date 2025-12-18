"""
QUESTION:
Create a function `filter_primes_divisible_by_six` that filters out the integers from a given list that are divisible by 6 and are also prime numbers. The function should return a list of these numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes_divisible_by_six(nums):
    return [num for num in nums if num % 6 == 0 and is_prime(num)]