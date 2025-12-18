"""
QUESTION:
Write a function `find_nth_fibonacci` that takes three parameters: `lower`, `upper`, and `n`. The function should return the nth Fibonacci number within the range defined by `lower` and `upper` (inclusive). The Fibonacci sequence is considered to be within the range if the Fibonacci number is greater than or equal to `lower` and less than or equal to `upper`. If there are less than `n` Fibonacci numbers in the given range, the function should return `None`.
"""

def find_nth_fibonacci(lower, upper, n):
    fib_sequence = []
    a, b = 0, 1
    while b <= upper:
        if b >= lower:
            fib_sequence.append(b)
        a, b = b, a + b
    
    if len(fib_sequence) < n:
        return None
    else:
        return fib_sequence[n-1]