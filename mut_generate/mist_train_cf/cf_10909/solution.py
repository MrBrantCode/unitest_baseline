"""
QUESTION:
Create a function named `fibonacci(n)` that generates and returns the Fibonacci sequence up to the nth number. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence. For example, calling `fibonacci(100)` should return the Fibonacci sequence up to the 100th number.
"""

def fibonacci(n):
    fib_seq = [0, 1]  
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])  
    return fib_seq