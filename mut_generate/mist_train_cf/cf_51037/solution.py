"""
QUESTION:
Create a function called `fibonacci_sequence` that generates the Fibonacci sequence up to a given length n. The function should use a while loop and start with the first two numbers in the Fibonacci sequence, which are 0 and 1. It should calculate each subsequent number as the sum of the last two numbers in the sequence. The function should return a list of the first n numbers in the Fibonacci sequence.
"""

def fibonacci_sequence(n):
    """Generate the Fibonacci sequence up to a given length n."""
    fib = [0, 1]
    i = 2
    
    while i < n:
        fib.append(fib[i - 2] + fib[i - 1])
        i += 1
    
    return fib