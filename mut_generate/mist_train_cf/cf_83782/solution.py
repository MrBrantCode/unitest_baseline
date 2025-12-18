"""
QUESTION:
Create a function `fibonacci_divider` that takes a list of integers as input and returns two lists: one containing the Fibonacci numbers and the other containing the non-Fibonacci numbers from the input list. The function should use a helper function `is_fibonacci` to check if a number is a Fibonacci number or not.
"""

import math

def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return math.isqrt(x1) ** 2 == x1 or math.isqrt(x2) ** 2 == x2

def fibonacci_divider(arr):
    fibo = []
    non_fibo = []
    for i in arr:
        if is_fibonacci(i):
            fibo.append(i)
        else:
            non_fibo.append(i)
    return fibo, non_fibo