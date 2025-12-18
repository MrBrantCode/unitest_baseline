"""
QUESTION:
Create a function called `sum_of_prime_fibonacci` that calculates the sum of the Fibonacci series up to the nth term, including only prime numbers. The function should take an integer `n` as input and return the sum of prime Fibonacci numbers up to the nth term. The input `n` is relatively small since the Fibonacci sequence grows quickly and soon exceeds the range of commonly used prime numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_prime_fibonacci(n):
    """
    This function calculates the sum of the Fibonacci series up to the nth term, 
    including only prime numbers.

    Parameters:
    n (int): The nth term of the Fibonacci series.

    Returns:
    int: The sum of prime Fibonacci numbers up to the nth term.
    """
    sum = 0
    for i in range(n):
        fib = fibonacci(i)
        if is_prime(fib):
            sum += fib
    return sum