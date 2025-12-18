"""
QUESTION:
Create a function called `fibonacci(n)` that generates the Fibonacci sequence up to `n` squared terms. The function should take an integer `n` as input and yield each Fibonacci number until it has generated `n` squared numbers.
"""

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        count += 1
        if count > n*n:
            return
        yield a