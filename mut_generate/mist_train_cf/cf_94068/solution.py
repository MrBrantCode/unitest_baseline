"""
QUESTION:
Write a function named `highest_prime_palindrome(num)` that takes in a positive integer `num` and returns the highest prime number that is both a palindrome and can be divided by `num`. The function should be able to handle positive integers as inputs and return an integer as output.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def entrance(num):
    max_prime_palindrome = 0
    for i in range(num, 1, -1):
        if not is_prime(i):
            continue
        if is_palindrome(i):
            max_prime_palindrome = max(max_prime_palindrome, i)
    return max_prime_palindrome