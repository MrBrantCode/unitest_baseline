"""
QUESTION:
Create three functions: `is_prime(n)`, `is_palindrome(n)`, and `find_primes(n)`.

`is_prime(n)` should determine if a given integer `n` is prime, with a time complexity of O(sqrt(n)) and a space complexity of O(1). It should return `True` if `n` is prime and `False` otherwise.

`is_palindrome(n)` should check if a given integer `n` is a palindrome, with a time complexity of O(log10(n)) and a space complexity of O(1). It should return `True` if `n` is a palindrome and `False` otherwise. The function should handle edge cases where `n` is negative, zero, or a non-integer.

`find_primes(n)` should find and print all prime numbers between 0 and a given number `n`, where `n` can be up to 1 billion, with a time complexity of O(sqrt(n)) and a space complexity of O(1). It should return a list of prime numbers or an error message if `n` is not a non-negative integer.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= math.isqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True

def is_palindrome(n):
    if not isinstance(n, int) or n < 0:
        return False
    if n == 0:
        return True
    num_digits = math.floor(math.log10(n)) + 1
    for i in range(num_digits // 2):
        if (n // 10**i) % 10 != (n // 10**(num_digits - i - 1)) % 10:
            return False
    return True

def find_primes(n):
    if not isinstance(n, int) or n < 0:
        return "Error: n must be a non-negative integer"
    primes = []
    i = 0
    while i <= n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes