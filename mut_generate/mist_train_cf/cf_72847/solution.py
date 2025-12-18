"""
QUESTION:
Develop a function called `find_highest_fibonacci` that takes a list of integers as input and returns the highest Fibonacci number in the list. A Fibonacci number is a number where either (5*n^2 + 4) or (5*n^2 - 4) is a perfect square. If no Fibonacci number exists in the list, return -1.
"""

import math

def is_square(x):
    s = int(math.sqrt(x))
    return s*s == x

def is_fibonacci(n):
    return is_square(5*n*n + 4) or is_square(5*n*n - 4)

def find_highest_fibonacci(numbers):
    max_fib = -1
    for number in numbers:
        if is_fibonacci(number) and number > max_fib:
            max_fib = number
    return max_fib