"""
QUESTION:
Write a function named `display_prime_fibonacci_reverse` that prints the first 50 prime numbers in the Fibonacci sequence in reverse order. The function should use a helper function named `is_prime` to check if a number is prime, which must have a time complexity of O(sqrt(n)). Additionally, the function should use memoization to optimize the calculation of Fibonacci numbers and handle arbitrarily large numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        fib_cache[n] = n
        return n
    fib = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = fib
    return fib

def display_prime_fibonacci_reverse(n):
    prime_fibonacci = []
    count = 0
    i = 0
    while count < n:
        fib = fibonacci(i)
        if is_prime(fib):
            prime_fibonacci.append(fib)
            count += 1
        i += 1
    prime_fibonacci.reverse()
    for num in prime_fibonacci:
        print(num)