"""
QUESTION:
Write a function named `fib_or_prime` that calculates the `n`th Fibonacci number if `n` is not a prime number. However, if `n` is a prime number, the function should return the `n`th prime number instead. The input `n` is in the range `0 <= n <= 30`. The function should use a helper function `is_prime` to check if a number is prime, and another helper function `nth_prime` to find the `n`th prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib_or_prime(n):
    if is_prime(n):
        return nth_prime(n)  
    else:
        return fib(n)