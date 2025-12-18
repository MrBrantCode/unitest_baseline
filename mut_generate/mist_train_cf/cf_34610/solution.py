"""
QUESTION:
Implement a function `sum_even_fibonacci(limit)` that takes an integer `limit` as input and returns the sum of all even Fibonacci numbers less than or equal to the given limit. The Fibonacci sequence starts with 1 and 2, and each subsequent number is the sum of the two preceding ones.
"""

def sum_even_fibonacci(limit):
    a, b = 1, 2
    even_sum = 0
    while b <= limit:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum