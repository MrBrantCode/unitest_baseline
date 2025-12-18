"""
QUESTION:
Write a function named `print_primes(n)` to print all prime numbers between 1 and `n` without using a loop. The time complexity should be O(log n) and the space complexity should be O(1). You cannot use any mathematical functions or libraries to check for prime numbers; only basic arithmetic operations and logical operators are allowed.
"""

def print_primes(n, i=None):
    if i is None:
        i = n
    if i < 2:
        return
    if is_prime(i):
        print(i)
    print_primes(n, i - 1)

def is_prime(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)