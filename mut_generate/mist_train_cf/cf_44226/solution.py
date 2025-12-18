"""
QUESTION:
Create a function `fibonacci(n)` that calculates and returns the Fibonacci series up to n numbers. The function should generate the series by adding the last two numbers in the sequence to get the next number. The initial two numbers in the sequence should be 0 and 1.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence