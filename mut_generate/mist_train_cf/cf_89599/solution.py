"""
QUESTION:
Write a function named `display_prime_fibonacci_reverse` to display the Fibonacci sequence up to the nth term where each term is a prime number, in reverse order. This function should use a helper function named `is_prime` to check if a number is prime with a time complexity of O(sqrt(n)) and another helper function named `fibonacci` that uses memoization to optimize the calculation of Fibonacci numbers. The `display_prime_fibonacci_reverse` function should be able to handle cases where the nth prime Fibonacci number exceeds the maximum value that can be represented by the integer data type.
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