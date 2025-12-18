"""
QUESTION:
Create a function called `fibonacci_series(limit)` that generates Fibonacci numbers up to a given input limit. The function should return a list of Fibonacci numbers and their sum. The input limit must be a positive integer. If the limit is not a positive integer, return an error message.
"""

def fibonacci_series(limit):
    if not isinstance(limit, int) or limit <= 0:
        return "Invalid input! Limit must be a positive integer."
    
    fib_series = []
    a, b = 0, 1
    fib_sum = 0
    
    while a <= limit:
        fib_series.append(a)
        fib_sum += a
        a, b = b, a + b
    
    return fib_series, fib_sum