"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. Use this function to generate a list of the first 1000 prime numbers. The function should be efficient enough to handle large numbers and the output should be a list of integers.
"""

def entrance(n):
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