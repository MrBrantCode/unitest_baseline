"""
QUESTION:
Implement a function `even_fibonacci_sum(limit)` that calculates the sum of all even Fibonacci numbers less than or equal to the given integer `limit`, where the Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
"""

def even_fibonacci_sum(limit):
    fib1, fib2 = 0, 1
    even_sum = 0
    while fib2 <= limit:
        if fib2 % 2 == 0:
            even_sum += fib2
        fib1, fib2 = fib2, fib1 + fib2
    return even_sum