"""
QUESTION:
Create a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth number using an iterative approach without recursion. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    # Initializing the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generating the Fibonacci sequence iteratively
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence[:n]