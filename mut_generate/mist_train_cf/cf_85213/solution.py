"""
QUESTION:
Create a function `fibonacci_series(min_value, max_value)` that constructs and returns a list of Fibonacci numbers within the range of `min_value` and `max_value` (inclusive). The function should start generating Fibonacci numbers from the beginning of the sequence (0 and 1) and stop when the generated number exceeds `max_value`.
"""

def fibonacci_series(min_value, max_value):
    fib_series = []
    a, b = 0, 1
    while a <= max_value:
        if a >= min_value:
            fib_series.append(a)
        a, b = b, a + b
    return fib_series