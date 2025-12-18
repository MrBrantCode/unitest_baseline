"""
QUESTION:
Write a function `highest_prime_palindrome` that takes a positive integer as input and returns the highest prime number that is both a palindrome and can be divided by the given number. The function should only consider prime numbers less than or equal to the input number.
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

def highest_prime_palindrome(num):
    max_prime_palindrome = 0
    for i in range(num, 1, -1):
        if not is_prime(i):
            continue
        if is_palindrome(i) and num % i == 0:
            return i
    return max_prime_palindrome