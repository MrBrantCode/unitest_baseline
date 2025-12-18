"""
QUESTION:
Create a function `find_largest_fibonacci` that takes a list of integers as input and returns the largest Fibonacci number in the list. The function should be able to handle lists with up to a million integers and should operate in linear time complexity, O(n).
"""

import math

def is_square(N):
    return math.isqrt(N) ** 2 == N

def is_fibonacci(n):
    return is_square(5*n*n + 4) or is_square(5*n*n - 4)

def find_largest_fibonacci(lst):
    max_fib = -1
    for num in lst:
        if is_fibonacci(num):
            max_fib = max(max_fib, num)
    return max_fib