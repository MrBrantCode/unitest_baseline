"""
QUESTION:
Implement a function `evenFibonacciSum(limit)` that calculates the sum of all even Fibonacci numbers less than or equal to a given integer `limit`. The function should return the total sum of these numbers. Note that the Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. The function must only consider numbers in the sequence that are even and do not exceed the given limit.
"""

def evenFibonacciSum(limit):
    a, b = 0, 1
    total_sum = 0
    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum