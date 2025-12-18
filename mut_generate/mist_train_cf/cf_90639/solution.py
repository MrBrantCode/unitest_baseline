"""
QUESTION:
Write a recursive function `fibonacci(n)` to calculate the nth number in the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. The input `n` is the index of the Fibonacci sequence and is a non-negative integer. The function should return the value at the nth index in the Fibonacci sequence.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)