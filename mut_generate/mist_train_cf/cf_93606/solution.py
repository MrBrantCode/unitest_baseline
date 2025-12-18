"""
QUESTION:
Create a function `display_primes(a, b)` that prints all prime numbers between `a` and `b` (inclusive) that are also palindromic primes but not perfect squares. The function should use helper functions `is_palindrome(n)` and `is_prime(n)` to check for palindromes and primes, respectively.
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
        if is_palindrome(num) and is_prime(num) and not int(num**0.5)**2 == num:
            print(num)