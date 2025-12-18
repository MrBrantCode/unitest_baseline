"""
QUESTION:
Write a function `remove_largest_prime` that takes a list of integers as input, finds the largest prime number in the list, and returns the modified list with all occurrences of the largest prime number deleted.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_largest_prime(nums):
    primes = [num for num in nums if is_prime(num)]
    if primes:
        largest_prime = max(primes)
        return [num for num in nums if num != largest_prime]
    return nums