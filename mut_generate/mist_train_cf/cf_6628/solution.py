"""
QUESTION:
Create a function `sum_of_squares(k, n)` that takes two positive integers `k` and `n` as input, and returns the sum of the squares of even numbers between `k` and `n` (inclusive) that are also divisible by 3.
"""

def sum_of_squares(k, n):
    sum = 0
    for i in range(k, n+1):
        if i % 2 == 0 and i % 3 == 0:
            sum += i ** 2
    return sum