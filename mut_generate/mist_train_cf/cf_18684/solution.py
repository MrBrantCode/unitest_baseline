"""
QUESTION:
Write a function `is_prime(n)` to determine whether a given number `n` is prime. Additionally, write a function `print_primes(n)` to print all the prime numbers between 1 and `n`. The solution should have a time complexity of O(n * sqrt(n)) and efficiently handle large numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(n):
    for i in range(1, n+1):
        if is_prime(i):
            print(i)