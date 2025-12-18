"""
QUESTION:
Create a function `find_closest_fibonacci` that takes an integer `num` as input and returns the closest Fibonacci number that is smaller than `num`. If `num` is a Fibonacci number, return `num`. The function should have a time complexity of O(log(n)) and a space complexity of O(1).
"""

import math

def find_closest_fibonacci(num):
    if num <= 0:
        return 0

    fib_prev = 0
    fib_curr = 1
    while fib_curr <= num:
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    return fib_prev