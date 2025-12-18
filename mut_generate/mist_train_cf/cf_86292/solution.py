"""
QUESTION:
Create a function `display_primes(a, b)` that displays all prime numbers between the given range `a` and `b` (inclusive) that are also palindromes and not perfect cubes. The function should exclude prime numbers that are perfect cubes.
"""

def display_primes(a, b):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(a, b + 1):
        if is_palindrome(num) and is_prime(num):
            cube_root = int(num ** (1/3))
            if cube_root ** 3 != num:
                print(num)