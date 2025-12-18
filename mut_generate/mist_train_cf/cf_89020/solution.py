"""
QUESTION:
Generate a list of the first 10 prime numbers that are not palindromic and do not have a prime number of digits. The list should be sorted in descending order. Define helper functions `is_prime(n)` to check if a number is prime and `is_palindromic(n)` to check if a number is palindromic. The list comprehension should be contained within a function named `primes_list`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindromic(n):
    return str(n) == str(n)[::-1]

def primes_list():
    return [n for n in range(1000, 1, -1) if is_prime(n) and not is_palindromic(n) and not is_prime(len(str(n)))][:10]