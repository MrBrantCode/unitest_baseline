"""
QUESTION:
Create a function `is_prime_and_palindrome(n)` that takes an integer `n` as input, where `2 ≤ n ≤ 10^9`. The function should return `True` if `n` is both a prime number and a palindrome, and `False` otherwise. The function should have a time complexity of O(sqrt(n)).
"""

import math

def is_prime_and_palindrome(n):
    if n < 2:
        return False

    # Check if n is a prime number
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    # Check if n is a palindrome
    return str(n) == str(n)[::-1]