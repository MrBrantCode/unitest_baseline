"""
QUESTION:
Create a function `fib(n)` that calculates the sum of even-valued terms in the Fibonacci sequence that do not exceed the given number `n`. The Fibonacci sequence starts with 1 and 2. The function should return the sum of even-valued terms.
"""

def fib(n):
    a, b = 1, 2
    sum = 0
    while a <= n:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum