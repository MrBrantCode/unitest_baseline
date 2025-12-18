"""
QUESTION:
Write a function `generate_fibonacci(max_value)` to generate all Fibonacci numbers within a given numerical range. The function should take an integer `max_value` as input and return a list of Fibonacci numbers less than or equal to `max_value`. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def generate_fibonacci(max_value):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= max_value:
        fib.append(fib[-1] + fib[-2])
    return fib