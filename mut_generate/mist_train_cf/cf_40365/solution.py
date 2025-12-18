"""
QUESTION:
Create a function `fib_even_sum(limit)` that calculates the sum of all even-valued terms in the Fibonacci sequence up to the given limit. The input `limit` is a positive integer (0 < limit <= 10^6), and the function should efficiently handle large input values within a reasonable time frame.
"""

def fib_even_sum(limit):
    sum_even = 0
    a, b = 0, 1
    while b <= limit:
        if b % 2 == 0:
            sum_even += b
        a, b = b, a + b
    return sum_even