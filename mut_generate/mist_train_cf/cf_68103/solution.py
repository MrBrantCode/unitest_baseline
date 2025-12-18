"""
QUESTION:
Write a Python function named `longest_prime_subarray` that takes an array of integers as input and returns the start and end indices of the longest continuous subarray consisting only of prime numbers. The function should use a helper function named `is_prime` to check if a number is prime. The `is_prime` function should return `True` if the number is prime and `False` otherwise. The `longest_prime_subarray` function should return the start and end indices as a tuple.
"""

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def longest_prime_subarray(arr):
    """Find the longest continuous subarray of prime numbers."""
    start = 0
    end = 0
    max_length = 0
    max_start = 0
    max_end = 0

    for i in range(len(arr)):
        if is_prime(arr[i]):
            end = i
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_start = start
                max_end = end
        else:
            start = i + 1

    return max_start, max_end