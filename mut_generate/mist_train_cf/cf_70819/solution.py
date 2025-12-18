"""
QUESTION:
Write a function `fibo_square_counter` that takes two parameters `start` and `end` and returns the count of Fibonacci numbers within the range `[start, end]` that are also perfect squares. The function should only consider positive integers in the Fibonacci sequence.
"""

from math import isqrt

def is_perfect_square(n):
    return n == isqrt(n) ** 2

def fibo_square_counter(start, end):
    a, b = 0, 1
    count = 0
    while a <= end:
        if a >= start and is_perfect_square(a):
            count += 1
        a, b = b, a + b
    return count