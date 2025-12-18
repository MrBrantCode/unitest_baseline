"""
QUESTION:
Write a function `print_primes(n)` to print all prime numbers between 1 and `n` without using any loops, mathematical functions, or libraries. The function should have a time complexity of O(log n) and a space complexity of O(1). The function should only use basic arithmetic operations and logical operators to check for prime numbers.
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