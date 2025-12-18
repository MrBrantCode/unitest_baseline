"""
QUESTION:
Write a function `fibonacci(n)` that prints the Fibonacci series up to a given number `n`, but only includes numbers that are prime. The function should only print numbers that are both Fibonacci numbers and prime numbers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if is_prime(a):
            print(a, end=' ')
        a, b = b, a + b