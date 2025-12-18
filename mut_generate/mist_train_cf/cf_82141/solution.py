"""
QUESTION:
Write a function `fibonacci_sequence(n)` that takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence. Then use this function to create a new list where all elements greater than 5 in the given list are replaced with their corresponding Fibonacci sequence value. Assume the Fibonacci sequence starts with 0 and 1.
"""

def fibonacci_sequence(n):
    fib_sequence=[0,1]
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        fib_sequence.append(b)
    return fib_sequence[n]