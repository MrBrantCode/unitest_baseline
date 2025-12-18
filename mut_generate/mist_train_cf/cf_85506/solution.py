"""
QUESTION:
Implement a function `is_prime(n)` to check if a number `n` is prime. The function should return `False` for non-integer data types, negative numbers, the number zero, and non-prime numbers, and `True` otherwise. Use this function to filter out prime numbers from a given list.
"""

def is_prime(n):
    # Check if argument is integer
    if not isinstance(n, int):
        return False
    # Check if argument is negative or 0
    if n <= 0:
        return False
    # 1 is not prime
    if n == 1:
        return False
    # 2 is prime
    if n == 2:
        return True
    # Check divisibility for numbers up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True