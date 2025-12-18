"""
QUESTION:
Implement a function `even_fibonacci_sum(limit)` that takes an integer `limit` as input and returns the sum of all even Fibonacci numbers less than or equal to the given limit. The Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
"""

def even_fibonacci_sum(limit):
    a, b = 0, 1
    total_sum = 0
    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum