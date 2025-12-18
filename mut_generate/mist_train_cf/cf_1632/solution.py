"""
QUESTION:
Write a function named `nth_prime` that uses recursion to calculate the nth prime number. The function should not hard-code any prime numbers and must include error handling for potential input errors or exceptions. Additionally, write a function named `fibonacci` that uses recursion to calculate the nth Fibonacci number. Then, use these functions to find and print the 42nd prime number and the 42nd Fibonacci number.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n, count=0, num=2):
    if is_prime(num):
        count += 1
    if count == n:
        return num
    return nth_prime(n, count, num + 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)