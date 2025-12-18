"""
QUESTION:
Write a function `find_nth_fibonacci(lower, upper, n)` that finds the nth Fibonacci number within a given range. The function should take three parameters: `lower` and `upper`, which define the range, and `n`, which is the position of the Fibonacci number to find. The function should return the nth Fibonacci number in the range if it exists, or `None` otherwise. The Fibonacci sequence should be generated up to the upper bound of the range.
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