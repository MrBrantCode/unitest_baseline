"""
QUESTION:
Create a function `display_primes(a, b)` to display all prime numbers between a given range `a` and `b` (inclusive), where the numbers are both palindromes and not perfect cubes.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_primes(a, b):
    for num in range(a, b + 1):
        if is_palindrome(num) and is_prime(num):
            cube_root = int(num ** (1/3))
            if cube_root ** 3 != num:
                print(num)