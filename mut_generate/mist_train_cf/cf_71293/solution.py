"""
QUESTION:
Create a function `prime_fibonacci(n)` that takes an integer `n` as input and returns a list of all Fibonacci numbers that are also prime numbers within the range 1 to `n`. The function should use helper functions `is_prime(n)` to check if a number is prime and `is_fibonacci(n)` to check if a number is a Fibonacci number.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

def is_fibonacci(n):
    if n <= 0:
        return False
    x = 0
    y = 1
    while y < n:
        z = y
        y = y + x
        x = z
    return y == n

def prime_fibonacci(n):
    result = []
    for i in range(1, n+1):
        if is_prime(i) and is_fibonacci(i):
            result.append(i)
    return result