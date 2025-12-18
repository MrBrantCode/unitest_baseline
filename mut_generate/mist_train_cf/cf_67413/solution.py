"""
QUESTION:
Write a function `fib(n)` that returns the first `n` natural numbers in the Fibonacci series, where `n` is a positive integer. Implement the function using iterative calculation and ensure it handles base cases where `n` is less than or equal to 2. The function should return an error message if `n` is less than or equal to 0.
"""

def fib(n):
    if n <= 0:
       return "Incorrect input"
    elif n == 1:
       return [0]
    elif n == 2:
       return [0, 1]
    else:
       fib_seq = [0, 1]
       while len(fib_seq) < n:
           fib_seq.append(fib_seq[-1] + fib_seq[-2])
       return fib_seq