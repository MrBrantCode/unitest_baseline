"""
QUESTION:
Write a function `factorial_prime(n)` that prints all prime numbers from 1 to `n` using a recursive function paradigm. The function should utilize another function `is_prime(n)` to check whether a given number `n` is prime or not. Note that `n` is a positive integer and `n` can be up to 100.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorial_prime(n):
    for i in range(1, n+1):
        if is_prime(i):
            print(i)