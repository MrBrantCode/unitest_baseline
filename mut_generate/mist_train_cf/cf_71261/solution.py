"""
QUESTION:
Write a function `rearrange(arr)` that takes an array of integers as input and returns the array with all prime numbers on the left and non-prime numbers on the right. The order of prime and non-prime numbers within their respective groups can be arbitrary.
"""

def is_prime(n):
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

def rearrange(arr):
    primes = [val for val in arr if is_prime(val)]
    non_primes = [val for val in arr if not is_prime(val)]
    return primes + non_primes