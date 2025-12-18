"""
QUESTION:
Write a function named `factorial_with_memory_limit` that takes a single positive integer or decimal argument `n` and returns its factorial if `n` is a non-prime integer. The function should return `None` if `n` is a decimal, prime, or if the memory usage exceeds 1 MB during the factorial calculation. The function should be optimized to minimize memory usage and reduce the time complexity of the factorial calculation.
"""

import sys

def factorial_with_memory_limit(n):
    # Check if input is decimal
    if n != int(n):
        return None

    # Check if input is prime
    if is_prime(n):
        return None

    # Check if input is less than or equal to 1
    if n <= 1:
        return 1

    # Initialize variables
    factorial = 1
    memory_limit = 1000000  # 1 MB in bytes
    memory_usage = sys.getsizeof(factorial)

    # Calculate factorial
    for i in range(2, n + 1):
        factorial *= i

        # Check memory usage
        memory_usage += sys.getsizeof(i)
        if memory_usage > memory_limit:
            return None

    return factorial

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True