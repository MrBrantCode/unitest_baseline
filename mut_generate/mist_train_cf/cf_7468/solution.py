"""
QUESTION:
Write a function `generate_fibonacci(n)` that generates the Fibonacci sequence up to the nth number without using loops or recursion, with a time complexity of O(n) and a space complexity of O(1). The function should return a list of integers.
"""

import math

def generate_fibonacci(n):
    if n <= 0:
        return []

    fibonacci = []
    for i in range(1, n+1):
        fibonacci.append(int(((1/math.sqrt(5)) * (((1 + math.sqrt(5)) / 2)**i - ((1 - math.sqrt(5)) / 2)**i)) + 0.5))

    return fibonacci