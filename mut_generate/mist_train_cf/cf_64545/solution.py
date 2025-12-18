"""
QUESTION:
Create a recursive function called `fibonacci(n)` to calculate the n-th term of the Fibonacci sequence where each number is the sum of the two preceding ones. The input `n` is a positive integer, and the function should return the n-th term of the sequence.
"""

def fibonacci(n):
    if n <= 0:
        return "Input number should be positive"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)