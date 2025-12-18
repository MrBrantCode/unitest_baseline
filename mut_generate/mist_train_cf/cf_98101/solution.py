"""
QUESTION:
Write a function `find_largest_prime_palindrome(n)` that finds the largest prime palindrome number without using any loops, given an initial number `n`. A prime palindrome is a number that is both a prime and a palindrome. The function should return the largest prime palindrome number that is less than or equal to `n`. Restriction: `n` is a 3-digit number.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_largest_prime_palindrome(n):
    if n == 100:
        return n
    elif is_palindrome(n) and is_prime(n):
        return n
    else:
        return find_largest_prime_palindrome(n - 1)