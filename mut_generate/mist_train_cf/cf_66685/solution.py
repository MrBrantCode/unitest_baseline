"""
QUESTION:
Write a function `fibonacci(n)` to compute the nth term in the Fibonacci sequence, where the sequence is defined as: each term is the sum of the two preceding ones, with the first two terms being 0 and 1. The function should use recursion and handle cases where `n` is less than or equal to 0, and `n` is 1 or 2. The function should return the nth term in the sequence.
"""

def fibonacci(n):
    if n <= 0:
       return "Input should be positive integer."
    elif n == 1:
       return 0
    elif n == 2:
       return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)