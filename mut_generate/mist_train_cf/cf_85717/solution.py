"""
QUESTION:
Write a function `modified_fibonacci(steps)` that takes a string of steps as input, where 'F' represents a step forward and 'B' represents a step backward in a modified Fibonacci sequence, and returns the smallest possible `a_1` and `a_2` that begin with the given sequence.
"""

def modified_fibonacci(steps):
    seq = [1, 1]
    fib1 = 1
    fib2 = 1
    for s in reversed(steps):
        if s == 'F':
            while fib2 % 3 != 0:
                fib1, fib2 = fib2, fib2 + fib1
        if s == 'B':
            while fib2 % 2 == 0:
                fib1, fib2 = fib2, fib2 + fib1
        seq.append(fib2)
    return seq[-1:-3:-1]