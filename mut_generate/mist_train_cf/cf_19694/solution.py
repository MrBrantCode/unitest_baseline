"""
QUESTION:
Write a function named `find_seventh_prime` that takes an array of integers as input, iterates over the array, and returns the 7th prime number found. If there are less than 7 prime numbers in the array, return -1. The function should consider only prime numbers and ignore non-prime numbers.
"""

def find_seventh_prime(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for num in arr:
        if is_prime(num):
            prime_count += 1
            if prime_count == 7:
                return num
    return -1  # If there are less than 7 prime numbers in the array