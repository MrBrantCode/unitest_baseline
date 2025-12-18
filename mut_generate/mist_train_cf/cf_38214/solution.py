"""
QUESTION:
Implement a function `evenFibonacciSum(limit)` that takes an integer `limit` as input and returns the sum of all the even Fibonacci numbers less than or equal to the given limit.
"""

def entrance(limit):
    a, b = 0, 1
    total_sum = 0
    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum